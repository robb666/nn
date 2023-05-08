import os
import glob
import matplotlib.pyplot as plt
import cv2
import requests
import random
import numpy as np
import zipfile

import subprocess


SEED = 42
np.random.seed(SEED)

TRAIN = True
EPOCHS = 25


def download_file(url, save_name):
    url = url
    if not os.path.exists(save_name):
        file = requests.get(url)
        open(save_name, 'wb').write(file.content)
    else:
        print('File already present, skipping download...')


if not os.path.exists('roboflow_unzipped'):
    print('Downloading...')
    r = requests.get('https://public.roboflow.com/ds/xKLV14HbTF?key=aJzo7msVta')
    with open('roboflow.zip', 'wb') as f:
        f.write(r.content)

    with zipfile.ZipFile('./roboflow.zip', 'r') as zip_ref:
        zip_ref.extractall(os.getcwd() + '/roboflow_unzipped')
    os.remove('./roboflow.zip')
    os.chdir('./roboflow_unzipped')

    dirs = ['train', 'valid', 'test']

    for i, dir_name in enumerate(dirs):
        all_image_names = sorted(os.listdir(f"{dir_name}/images/"))
        for j, image_name in enumerate(all_image_names):
            if (j % 2) == 0:
                file_name = image_name.split('.jpg')[0]
                os.remove(f'{dir_name}/images/{image_name}')
                os.remove(f'{dir_name}/labels/{file_name}.txt')
else:
    print('Skipping download. Folder exists.')

class_names = ['Ambulance', 'Bus', 'Car', 'Motorcycle', 'Truck']
colors = np.random.uniform(0, 255, size=(len(class_names), 3))


def yolo2bbox(bboxes):
    xmin, ymin = bboxes[0] - bboxes[2] / 2, bboxes[1] - bboxes[3] / 2
    xmax, ymax = bboxes[0] + bboxes[2] / 2, bboxes[1] + bboxes[3] / 2
    return xmin, ymin, xmax, ymax


def plot_box(image, bboxes, labels):
    # Need the image height and width to denormalize the
    # bounding box
    h, w, _ = image.shape
    for box_num, box in enumerate(bboxes):
        x1, y1, x2, y2 = yolo2bbox(box)
        # denormalize the coordinates
        xmin = int(x1*w)
        ymin = int(y1*h)
        xmax = int(x2*w)
        ymax = int(y2*h)
        width = xmax - xmin
        height = ymax - ymin

        class_name = class_names[int(labels[box_num])]

        cv2.rectangle(
            image,
            (xmin, ymin), (xmax, ymax),
            color=colors[class_names.index(class_name)],
            thickness=2
        )

        font_scale = min(1, max(3, int(w/500)))
        font_thickness = min(2, max(10, int(w/50)))

        p1, p2 = (int(xmin), int(ymin)), (int(xmax), int(ymax))
        # Text width and height
        tw, th = cv2.getTextSize(
            class_name,
            0, fontScale=font_scale, thickness=font_thickness
        )[0]
        p2 = p1[0] + tw, p1[1] + -th -10
        cv2.rectangle(
            image,
            p1, p2,
            color=colors[class_names.index(class_name)],
            thickness=-1,
        )
        cv2.putText(
            image,
            class_name,
            (xmin+1, ymin-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            font_scale,
            (225, 225, 225),
            font_thickness
        )
    return image


# Function to plot images with the bounding boxes
def plot(image_paths, label_paths, num_samples):
    os.chdir('./roboflow_unzipped')
    all_training_images = glob.glob(image_paths)
    all_training_labels = glob.glob(label_paths)
    all_training_images.sort()
    all_training_labels.sort()

    num_images = len(all_training_images)

    plt.figure(figsize=(15, 12))
    for i in range(num_samples):
        j = random.randint(0, num_images-1)
        image = cv2.imread(all_training_images[j])
        with open(all_training_labels[j], 'r') as f:
            bboxes = []
            labels = []
            label_lines = f.readlines()
            for label_line in label_lines:
                label = label_line[0]
                bbox_string = label_line[2:]

                x_c, y_c, w, h = bbox_string.split(' ')
                x_c = float(x_c)
                y_c = float(y_c)
                w = float(w)
                h = float(h)
                bboxes.append([x_c, y_c, w, h])
                labels.append(label)
        result_image = plot_box(image, bboxes, labels)
        plt.subplot(2, 2, i+1)
        plt.imshow(result_image[:, :, ::-1])
        plt.axis('off')
    plt.subplots_adjust(wspace=0)
    plt.tight_layout()
    plt.show()


def set_res_dir():
    # Directory to store results
    res_dir_count = len(glob.glob('runs/train/*'))
    print(f'Current number of results directories: {res_dir_count}')
    if TRAIN:
        RES_DIR = f'results_{res_dir_count + 1}'
        print(RES_DIR)
    else:
        RES_DIR = f'results_{res_dir_count}'
    return RES_DIR


def monitor_tensorboard():
    import tensorflow as tf
    # %load_ext tensorboard
    # %tensorboard --logdir runs/train


# Clone YOLOv5 repo
if not os.path.exists('yolov5'):
    subprocess.run(['git', 'clone', 'https://github.com/ultralytics/yolov5.git'])

os.chdir('yolov5')



plot(image_paths='train/images/*',
     label_paths='train/labels/*',
     num_samples=4)


monitor_tensorboard()

RES_DIR = set_res_dir()
if TRAIN:




















