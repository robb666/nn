import os
from pathlib import Path
import glob
import time
import subprocess
import requests
import re
from creds import TOKEN
from pprint import pprint


# share_path = "/run/user/1000/gvfs/smb-share:server=192.168.1.12,share=e/zzzProjekty/labels yolo/dow rej"

# response = requests.get('http://localhost:8080/api/projects/',
response = requests.get('http://localhost:8080/api/projects/1/tasks/?page=1&page_size=200',
                        headers={'Authorization': TOKEN}).json()
images_range = len(response)

# pprint(response)

imgs_uploaded = set()

for idx in range(images_range):
    strip_LS_id = re.search('([a-z0-9]+-)?(.+)', response[idx]['data']['image'])
    imgs_uploaded.add(strip_LS_id.group(2))

print(imgs_uploaded)

print()
print()
print()

data_path = Path("/run/user/1000/gvfs/smb-share:server=192.168.1.12,share=e/zzzProjekty/labels yolo/dow rej")
reg_certificates = os.listdir(data_path)

print(reg_certificates)

# share_path = "/run/user/1000/gvfs/smb-share:server=192.168.1.12,share=e/zzzProjekty/labels yolo/dow rej"
# cd "/home/robb/Desktop/labels yolo/dow rej" && python3 -m http.server 8082

subprocess.run(['python', 'duplicate_helper.py', data_path, '&&', 'python3', '-m', 'http.server', '8082'])

json_data = [
    {
        'image': 'http://0.0.0.0:8082/20180607_065400.jpg'
    }
]

print(json_data)

# response = requests.post('http://localhost:8080/api/projects/1/import',
#                          headers={'Authorization': TOKEN},
#                          json=json_data).json()

# for img in reg_certificates:
#     if img not in imgs_uploaded:
#         print(img)



# pprint(response)

