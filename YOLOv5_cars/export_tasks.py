#!../.env/bin/python3
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

    if response.status_code == 200:
        tasks = response.json()
        for task in tasks:
            task_id = task['id']
            image_src = task['data']['image']
            annotations = task['annotations']

            image_filename = f'{task_id}.jpg'
            if image_src.startswith('http'):
                image_data = requests.get(image_src).content
                with open(images_dir / image_filename, 'wb') as image_file:
                    image_file.write(image_data)
            else:
                shutil.copy(get_local_path(image_src), images_dir / image_filename)

            label_filename = f'{task_id}.txt'
            with open(labels_dir / label_filename, 'w') as label_file:
                for annotation in annotations:
                    label_file.write(f'{annotation}\n')
            print(image_src)
            break
        return '\nTasks exported successfully.'
    else:
        return f'Error: {response.status_code} -> {response.text}'
