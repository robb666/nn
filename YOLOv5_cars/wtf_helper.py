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
from pprint import pprint


def get_export():

    images_dir = Path('/home/robb/Desktop/output/images')
    labels_dir = Path('/home/robb/Desktop/output/labels')

    print(images_dir.is_dir())

    shutil.copy(images_dir / 'output', labels_dir)



    # response = requests.get('http://localhost:8080/api/projects/1/export',
    #                         timeout=10,
    #                         headers={
    #                             'Authorization': TOKEN,
    #                             'Content-Type': 'application/json'
    #                             },
    #                         )
    #
    # # pprint(response)
    #
    # if response.status_code == 200:
    #     tasks = response.json()
    #     for task in tasks:
    #         task_id = task['id']
    #         image_url = task['data']['image']
    #         print(image_url)
    #         annotations = task['annotations']
    #
    #         image_filename = f'{task_id}.jpg'
    #         if image_url.startswith('http'):
    #             image_data = requests.get(image_url).content
    #         else:
    #             image_data = shutil.copy(image_url)
    #
    #         with open(images_dir / image_filename, 'wb') as image_file:
    #             image_file.write(image_data)
    #
    #         label_filename = f'{task_id}.txt'
    #         with open(labels_dir / label_filename) as label_file:
    #             for annotation in annotations:
    #                 label_file.write(f'{annotation}\n')
    #
    #     print('Task exported successfully.')
    # else:
    #     print(f'Error: {response.status_code} -> {response.text}')


    # pprint(response)


    # with open(str(output), 'wb') as f:
    #     f.write(response.content)



    # subprocess.run(['label-studio', 'export', '1', 'JSON', f'path={output}'])


    # subprocess.run(['curl', '-X', 'GET', 'http://localhost:8080/api/projects/1/export?exportType=YOLO',
    #                 '-H' f'Authorization: {TOKEN}', '--output', '/home/robb/Desktop/output/annotations.json'])


    # return response


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


print(get_export())

# check_Label_Studio_images()
# images_vs_labels()

