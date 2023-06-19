import torch
import torchvision.transforms as transforms
from PIL import Image
import os
import re
from pathlib import Path
import glob
import time
import requests
from creds import TOKEN
import cv2
import subprocess
import shutil
import random
import numpy as np
from natsort import natsorted
from pprint import pprint
from label_studio_tools.core.utils.io \
    import get_local_path


def box_iou_batch(boxes_a: np.ndarray, boxes_b: np.ndarray) -> np.ndarray:

    def box_area(box):
        return (box[2] - box[0]) * (box[3] - box[1])

    area_a = box_area(boxes_a.T)
    area_b = box_area(boxes_b.T)

    top_left = np.maximum(boxes_a[:, None, :2], boxes_b[:, :2])
    bottom_right = np.minimum(boxes_a[:, None, 2:], boxes_b[:, 2:])

    area_inter = np.prod(np.clip(bottom_right - top_left, a_min=0, a_max=None), 2)

    return area_inter / (area_a[:, None] + area_b - area_inter)


def non_max_suppression(predictions: np.array, iou_threshold: float = 0.5) -> np.ndarray:

    rows, columns = predictions.shape

    sort_index = np.flip(predictions[:, 4].argsort())
    predictions = predictions[sort_index]

    boxes = predictions[:, 4]
    categories = predictions[:, 5]
    ious = box_iou_batch(boxes, boxes)
    ious = ious - np.eye(rows)

    keep = np.ones(rows, dtype=bool)

    for index, (iou, category) in enumerate(zip(ious, categories)):
        if not keep[index]:
            continue

        condition = (iou > iou_threshold) & (categories == category)
        keep = keep & ~condition

    return keep[sort_index.argsort()]


"""
model = torch.hub.load('./yolov5', 'custom', path='yolov5/runs/train/results_14/weights/best.pt', source='local')
cap = cv2.VideoCapture(0)
while cap.isOpened():
    return_, frame = cap.read()
    results = model(frame)
    results = non_max_suppression(results.detach().cpu().numpy())
    cv2.imshow('YOLO', np.squeeze(results.render()))
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
"""


def train_test_valid_split():
    train_dir, test_dir, valid_dir = resolve_directories()

    images_dir = Path('/home/robb/Desktop/output/images')
    labels_dir = Path('/home/robb/Desktop/output/labels')

    assert len(os.listdir(images_dir)) == len(os.listdir(labels_dir))

    dataset_size = len(os.listdir(images_dir))
    test_set = round(dataset_size * 0.2)
    valid_set = round(dataset_size * 0.1)

    random.seed(42)
    sorted_im_arr = natsorted(os.listdir(images_dir))
    # sorted_im_arr = sorted([int(x.rstrip('.jpg')) for x in os.listdir(images_dir)])
    # sorted_im_arr = [str(x) + '.jpg' for x in sorted_im_arr]
    # random.shuffle(sorted_im_arr)
    # print(sorted_im_arr)
    for test_image in sorted_im_arr[-test_set:]:
        shutil.move(images_dir / test_image, test_dir / 'images')
        sorted_im_arr.remove(test_image)

    for valid_image in sorted_im_arr[-valid_set:]:
        shutil.move(images_dir / valid_image, valid_dir / 'images')
        sorted_im_arr.remove(valid_image)

    for train_image in sorted_im_arr[:]:
        shutil.move(images_dir / train_image, train_dir / 'images')
        sorted_im_arr.remove(train_image)

    sorted_label_arr = natsorted(os.listdir(labels_dir))
    # sorted_label_arr = sorted([int(x.rstrip('.txt')) for x in os.listdir(labels_dir)])
    # sorted_label_arr = [str(x) + '.txt' for x in sorted_label_arr]
    # random.shuffle(sorted_im_arr)
    # print(sorted_label_arr)

    for test_label in sorted_label_arr[-test_set:]:
        shutil.move(labels_dir / test_label, test_dir / 'labels')
        sorted_label_arr.remove(test_label)

    for valid_label in sorted_label_arr[-valid_set:]:
        shutil.move(labels_dir / valid_label, valid_dir / 'labels')
        sorted_label_arr.remove(valid_label)

    for train_label in sorted_label_arr[:]:
        shutil.move(labels_dir / train_label, train_dir / 'labels')
        sorted_label_arr.remove(train_label)

    shutil.rmtree(images_dir)
    shutil.rmtree(labels_dir)

    return f'{dataset_size} images, {dataset_size} labels.\n\n' \
           f'From these:\n\n' \
           f'{test_set} test images, {test_set} test labels.\n' \
           f'{valid_set} validation images, {valid_set} validation labels.\n' \
           f'Left {dataset_size - test_set - valid_set} images with ' \
           f'{dataset_size - test_set - valid_set} labels to train.'


def resolve_directories():

    dataset_dir = Path('/home/robb/Desktop/output/dataset')
    dataset_dir.mkdir(exist_ok=True)

    train_dir = dataset_dir / 'train'
    test_dir = dataset_dir / 'test'
    valid_dir = dataset_dir / 'valid'
    train_dir.mkdir(exist_ok=True)
    test_dir.mkdir(exist_ok=True)
    valid_dir.mkdir(exist_ok=True)

    directory_list = [train_dir, test_dir, valid_dir]

    for directory in directory_list:
        images = directory / 'images'
        labels = directory / 'labels'
        images.mkdir(exist_ok=True)
        labels.mkdir(exist_ok=True)

    return directory_list


def get_export():
    images_dir = Path('/home/robb/Desktop/output/images')
    labels_dir = Path('/home/robb/Desktop/output/labels')
    images_dir.mkdir(exist_ok=True)
    labels_dir.mkdir(exist_ok=True)

    response = requests.get('http://localhost:8080/api/projects/1/export',
                            timeout=10,
                            headers={
                                'Authorization': TOKEN,
                                'Content-Type': 'application/json'
                                },
                            )

    if response.status_code == 200:
        tasks = response.json()
        for task in tasks:
            task_id = task['id']
            image_src = task['data']['image']
            annotations = task['annotations']
            # images
            image_filename = f'{task_id}.jpg'
            if image_src.startswith('http'):
                image_data = requests.get(image_src).content
                with open(images_dir / image_filename, 'wb') as image_file:
                    image_file.write(image_data)
            else:
                shutil.copy(get_local_path(image_src), images_dir / image_filename)
            # labels
            label_filename = f'{task_id}.txt'
            with open(labels_dir / label_filename, 'w') as label_file:
                for annotation in annotations:
                    results = annotation['result']
                    for result in results:
                        yolo_bbox = convert_ls2yolo(result)
                        label_file.write(f'{yolo_bbox}\n')
        return '\nTasks exported successfully.'
    else:
        return f'Error: {response.status_code} -> {response.text}'


def convert_ls2yolo(result):
    value = result['value']

    class_map = {
        'Dowód rej.': 0,
        'Kuczyk(i)': 1,
        'Lewy przód': 2,
        'Numer rej.': 3,
        'Prawy tył': 4,
        'Przebieg': 5,
        'VIN': 6,
        'Wnętrze': 7
    }

    if 'width' not in value or 'height' not in value:
        return None

    label = class_map[value['rectanglelabels'][0]]
    if all([key in value for key in ['x', 'y', 'width', 'height']]):
        return f"{label} " \
               f"{(value['x'] + value['width'] / 2) / 100.0} " \
               f"{(value['y'] + value['height'] / 2) / 100.0} " \
               f"{value['width'] / 100.0} " \
               f"{value['height'] / 100.0}" \



print(train_test_valid_split())
train_test_valid_split()









def check_Label_Studio_images():
    response = requests.get('http://localhost:8080/api/projects/1/tasks/?page=1&page_size=2000',
                            headers={'Authorization': TOKEN}).json()
    images_range = len(response)
    uploaded_images = set()
    for idx in range(images_range):
        strip_LS_id = re.search('(upload/1/[a-z0-9]+-|:8082/)(.+)', response[idx]['data']['image'])
        uploaded_images.add(strip_LS_id.group(2))

    print(uploaded_images)
    print(len(uploaded_images), 'images are in Label-Studio')
    return uploaded_images


def images_vs_labels():
    desktop = Path('/home/robb/Desktop/')

    images = desktop / 'images'
    labels = desktop / 'labels'

    images_list, labels_list = [], []

    for lab in os.listdir(labels):
        labels_list.append(lab.rstrip('.txt'))

    for img in os.listdir(images):
        # print(img)
        images_list.append(re.sub('.jpg|.jpeg|.jpe', '', img.rstrip('.jpg'), flags=re.I))

    for lab in labels_list:
        if lab not in images_list:
            print(lab)

    print(images_list)
    print(len(images_list), 'images after export')
    print(len(labels_list), 'labels after export')




# check_Label_Studio_images()
# images_vs_labels()

