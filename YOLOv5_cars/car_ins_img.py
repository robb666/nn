import os
import glob
import matplotlib.pyplot as plt
import cv2
import requests
import random
import numpy as np
import subprocess

print(os.getcwd())

SEED = 42
np.random.seed(SEED)

TRAIN = True
EPOCHS = 25
#
if not os.path.exists('roboflow.zip'):
    print('Downloading...')
    r = requests.get('https://public.roboflow.com/ds/xKLV14HbTF?key=aJzo7msVta')
    with open('roboflow.zip', 'wb') as f:
        f.write(r.content)
    subprocess.call(['unzip', '-o', './roboflow.zip', '-d', './roboflow_unzipped'])
    subprocess.call(['rm', 'roboflow.zip'])
else:

    print('Skipping download. Folder exists.')

# subprocess.call(['rm', 'roboflow.zip'])


# output = subprocess.run(["curl", "-I", "https://ubezpieczenia-magro.pl/"])
# print(output)