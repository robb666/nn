import os
from pathlib import Path
import glob
import time
import subprocess
import requests
import re
from creds import TOKEN
import http.server
import socketserver
import uuid
import time
from pprint import pprint



# response = requests.get('http://localhost:8080/api/projects/',
response = requests.get('http://localhost:8080/api/projects/1/tasks/?page=1&page_size=200',
                        headers={'Authorization': TOKEN}).json()
images_range = len(response)

# pprint(response)

imgs_uploaded = set()

for idx in range(images_range):
    strip_LS_id = re.search('[a-z0-9]+-(.+)', response[idx]['data']['image'])
    imgs_uploaded.add(strip_LS_id.group(1))

print(imgs_uploaded)

print()
print()
print()

data_path = Path("/run/user/1000/gvfs/smb-share:server=192.168.1.12,share=e/zzzProjekty/labels yolo/dow rej")
os.chdir(data_path)

reg_certificates = os.listdir(data_path)

print(reg_certificates)

# subprocess.run(['python3', 'http.server', '8082'])

# json_data = [
#     {
#         'image': 'http://0.0.0.0:8082/20180607_065400.jpg'
#     }
# ]

# print(json_data)

PORT = 8082
Handler = http.server.SimpleHTTPRequestHandler

# with socketserver.TCPServer(("", PORT), Handler) as httpd:
#     print("Serving at port", PORT)
#
#     time.sleep(2)
#
#     # for img in reg_certificates:
#     if '20180607_065400.jpg' not in imgs_uploaded:
#         uu_id = str(uuid.uuid1()).split('-')[0]
#         json_data = [
#             {
#                 'image': f'http://0.0.0.0:8082/{uu_id}-20180607_065400.jpg'
#             }
#         ]
#
#         print(json_data)
#         requests.post('http://localhost:8080/api/projects/1/import',
#                       headers={'Authorization': TOKEN},
#                       json=json_data).json()
#
#         time.sleep(2)







