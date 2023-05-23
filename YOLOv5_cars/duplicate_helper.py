import os
from pathlib import Path
import glob
import time
import subprocess
import requests
import re
from creds import TOKEN
from pprint import pprint


response = requests.get('http://localhost:8080/api/projects/1/tasks/?page=1&page_size=200',
                        headers={'Authorization': TOKEN}).json()
images_range = len(response)

print(images_range)

for img in range(images_range):
    pprint(re.search('[a-z0-9]+-(.+)', response[img]['data']['image']).group(1))


# data_path = Path('/home/robb/Desktop/labels yolo/dow rej')

# reg_certificates = os.listdir(data_path)


print()
print()



