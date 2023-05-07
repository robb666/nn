import os
import glob
import matplotlib.pyplot as plt
import cv2
import requests
import random
import numpy as np
import zipfile


SEED = 42
np.random.seed(SEED)

TRAIN = True
EPOCHS = 25


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
    pass
