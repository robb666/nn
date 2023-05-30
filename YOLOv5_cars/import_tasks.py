#!../.env/bin/python3
import os
from pathlib import Path
import requests
import re
import http.server
import socketserver
from creds import TOKEN


class MultiDirHandler(http.server.SimpleHTTPRequestHandler):
    data_path = Path("/run/user/1000/gvfs/smb-share:server=192.168.1.12,share=e/zzzProjekty/labels yolo")
    directories = [
        data_path / 'dow rej',
        data_path / 'kluczyki',
    ]

    def translate_path(self, path):
        # Map path to the corresponding file in multiple directories
        for directory in self.directories:
            full_path = os.path.join(directory, path[1:])
            if os.path.exists(full_path):
                return full_path
        return super().translate_path(path)


def merge(all_images, uploaded_images):
    PORT = 8082
    # Handler = http.server.SimpleHTTPRequestHandler
    Handler = MultiDirHandler
    i = 0
    print('top', os.getcwd())
    with socketserver.TCPServer(('', PORT), Handler) as httpd:
        print('\nServing at port:', PORT)
        for img in all_images:
            print(os.getcwd())
            if img not in uploaded_images and img not in ('Thumbs.db', 'desktop.ini'):
                json_data = {'image': f'http://0.0.0.0:{PORT}/{img}'}

                requests.post('http://localhost:8080/api/projects/1/import',
                              headers={'Authorization': TOKEN},
                              json=[json_data]).json()
                i += 1
        info = f'Uploaded {i} image(s).' if i > 0 else 'No images uploaded.'
        print(info)

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            httpd.shutdown()


def check_Label_Studio_images():
    response = requests.get('http://localhost:8080/api/projects/1/tasks/?page=1&page_size=2000',
                            headers={'Authorization': TOKEN}).json()
    images_range = len(response)
    uploaded_images = set()
    for idx in range(images_range):
        strip_LS_id = re.search('(upload/1/[a-z0-9]+-|:8082/)(.+)', response[idx]['data']['image'])
        uploaded_images.add(strip_LS_id.group(2))
    return uploaded_images


def check_local_dir():
    # data_path = Path("/run/user/1000/gvfs/smb-share:server=192.168.1.12,share=e/zzzProjekty/labels yolo/dow rej")
    data_path = Path("/run/user/1000/gvfs/smb-share:server=192.168.1.12,share=e/zzzProjekty/labels yolo")
    # os.chdir(data_path)
    all_certificates = os.listdir(data_path / 'dow rej') + os.listdir(data_path / 'kluczyki')

    return all_certificates


all_certificates = check_local_dir()
imgs_uploaded = check_Label_Studio_images()
# print(len(all_certificates))

merge(all_certificates, imgs_uploaded)
