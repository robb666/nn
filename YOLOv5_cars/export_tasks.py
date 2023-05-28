#!../.env/bin/python3
import os
from pathlib import Path
import requests
import shutil
import random
from natsort import natsorted
from creds import TOKEN
from label_studio_tools.core.utils.io \
    import get_local_path


def train_test_valid_split():
    train_dir, test_dir, valid_dir = resolve_directories()

    images_dir = Path('/home/robb/Desktop/output/images')
    labels_dir = Path('/home/robb/Desktop/output/labels')

    assert len(os.listdir(images_dir)) == len(os.listdir(labels_dir))

    dataset_size = len(os.listdir(images_dir))
    test_set = round(dataset_size * 0.2)
    valid_set = round(dataset_size * 0.1)

    # images
    random.seed(42)
    sorted_im_arr = natsorted(os.listdir(images_dir))
    # random.shuffle(sorted_im_arr)
    for test_image in sorted_im_arr[-test_set:]:
        shutil.move(images_dir / test_image, test_dir / 'images')
        sorted_im_arr.remove(test_image)

    for valid_image in sorted_im_arr[-valid_set:]:
        shutil.move(images_dir / valid_image, valid_dir / 'images')
        sorted_im_arr.remove(valid_image)

    for train_image in sorted_im_arr[:]:
        shutil.move(images_dir / train_image, train_dir / 'images')
        sorted_im_arr.remove(train_image)

    # labels
    sorted_label_arr = natsorted(os.listdir(labels_dir))
    # random.shuffle(sorted_im_arr)
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
           f'{dataset_size - test_set - valid_set} labels to train.\n'


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
            print(image_src)
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
        return '\nTasks exported successfully.\n'
    else:
        return f'\nError: {response.status_code} -> {response.text}'


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



print(get_export())
print(train_test_valid_split())

