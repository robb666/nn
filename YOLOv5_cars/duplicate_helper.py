#!../.env/bin/python3
import os
from pathlib import Path
import requests
import re
import http.server
import socketserver
from creds import TOKEN


def merge(all_images, uploaded_images):
    PORT = 8082
    Handler = http.server.SimpleHTTPRequestHandler
    i = 0
    with socketserver.TCPServer(('', PORT), Handler) as httpd:
        print('\nServing at port:', PORT)
        for img in all_images:
            if img not in uploaded_images:
                json_data = {'image': f'http://0.0.0.0:{PORT}/{img}'}

                requests.post('http://localhost:8080/api/projects/1/import',
                              headers={'Authorization': TOKEN},
                              json=[json_data]).json()
                i += 1
                break
        info = f'Uploaded {i} image(s).' if i > 0 else 'No images uploaded'
        print(info)

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            httpd.shutdown()


def check_Label_Studio_images():
    response = requests.get('http://localhost:8080/api/projects/1/tasks/?page=1&page_size=200',
                            headers={'Authorization': TOKEN}).json()
    images_range = len(response)
    uploaded_images = set()
    for idx in range(images_range):
        strip_LS_id = re.search('(upload/1/[a-z0-9]+-|:8082/)(.+)', response[idx]['data']['image'])
        uploaded_images.add(strip_LS_id.group(2))
    return uploaded_images


def check_local_dir():
    data_path = Path("/run/user/1000/gvfs/smb-share:server=192.168.1.12,share=e/zzzProjekty/labels yolo/dow rej")
    os.chdir(data_path)
    all_certificates = os.listdir(data_path)

    return all_certificates


all_certificates, imgs_uploaded = check_local_dir(), check_Label_Studio_images()
merge(all_certificates, imgs_uploaded)
