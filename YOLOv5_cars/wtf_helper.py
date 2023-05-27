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
from label_studio_tools.core.utils.io \
    import get_local_path


def get_export():
    images_dir = Path('/home/robb/Desktop/output/images')
    labels_dir = Path('/home/robb/Desktop/output/labels')

    response = requests.get('http://localhost:8080/api/projects/1/export',
                            timeout=10,
                            headers={
                                'Authorization': TOKEN,
                                'Content-Type': 'application/json'
                                },
                            )

    # pprint(response.json()[0])
    task = response.json()
    annotation = task[0]['annotations']
    # pprint(annotation)
    print()
    result = annotation[0]['result'][0]#['value']
    # pprint(result)

    return result


    # if response.status_code == 200:
    #     tasks = response.json()
    #     for task in tasks:
    #         task_id = task['id']
    #         image_src = task['data']['image']
    #         annotations = task['annotations']
    #
    #         image_filename = f'{task_id}.jpg'
    #         if image_src.startswith('http'):
    #             image_data = requests.get(image_src).content
    #             with open(images_dir / image_filename, 'wb') as image_file:
    #                 image_file.write(image_data)
    #         else:
    #             shutil.copy(get_local_path(image_src), images_dir / image_filename)
    #
    #         label_filename = f'{task_id}.txt'
    #         with open(labels_dir / label_filename, 'w') as label_file:
    #             for annotation in annotations:
    #                 label_file.write(f'{annotation}\n')
    #         print(image_src)
    #         break
    #     return '\nTasks exported successfully.'
    # else:
    #     return f'Error: {response.status_code} -> {response.text}'



# convert from LS percent units to pixels
def convert_from_ls(result):
    if 'original_width' not in result or 'original_height' not in result:
        return None

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

    value = result['value']
    w, h = result['original_width'], result['original_height']

    if all([key in value for key in ['x', 'y', 'width', 'height']]):
        return w * value['x'] / 100.0, \
               h * value['y'] / 100.0, \
               w * value['width'] / 100.0, \
               h * value['height'] / 100.0

print()
result = get_export()

print(convert_from_ls(result))




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

