#!../.env/bin/python3
import argparse
import os
import requests
import http.server
from pathlib import Path
import socketserver
import re
from creds import TOKEN


# class HandleAll(http.server.SimpleHTTPRequestHandler):
#     data_path = Path("/run/user/1000/gvfs/smb-share:server=192.168.1.12,share=e/zzzProjekty/labels yolo/all")
#     os.chdir(data_path)
#
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)


class HandleAll(http.server.SimpleHTTPRequestHandler):
    def __init__(self, PATH, *args, **kwargs):
        self.path = PATH
        os.chdir(self.path)
        super().__init__(*args, **kwargs)
        print(os.getcwd())



def merge(PATH, PORT, TOKEN):
    all_images = check_local_dir(PATH)
    uploaded_images = check_Label_Studio_images(PORT, TOKEN)

    Handler = HandleAll
    # Handler(PATH)

    i = 0
    with socketserver.TCPServer(('', PORT), Handler) as httpd:
        print('\nServing at port:', PORT)
        for img in all_images:
            if img not in uploaded_images and img not in ('Thumbs.db', 'desktop.ini'):
                json_data = {'image': f'http://0.0.0.0:{PORT}/{img}'}

                requests.post('http://localhost:8080/api/projects/1/import',
                              headers={'Authorization': TOKEN if 'Token' in TOKEN else f'Token {TOKEN}'},
                              json=[json_data]).json()
                i += 1
        info = f'Uploaded {i} image(s).' if i > 0 else 'No images uploaded.'
        print(info)

        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            httpd.shutdown()


def check_Label_Studio_images(PORT, TOKEN):
    """
    Checks if any objects were previously uploaded either from LS or via API. Use one PORT from the beginning.
    """
    response = requests.get('http://localhost:8080/api/projects/1/tasks/?page=1&page_size=2000',
                            headers={'Authorization': TOKEN if 'Token' in TOKEN else f'Token {TOKEN}'}).json()
    images_range = len(response)
    uploaded_images = set()
    for idx in range(images_range):
        strip_LS_id = re.search(f'(upload/1/[a-z0-9]+-|:{PORT}/)(.+)', response[idx]['data']['image'])
        if strip_LS_id:
            uploaded_images.add(strip_LS_id.group(2))
    return uploaded_images


def check_local_dir(PATH):
    data_path = Path(PATH)
    all_images = os.listdir(data_path)

    return all_images


def parse_options():
    parser = argparse.ArgumentParser()
    parser.add_argument('-path', '--PATH', type=str,
                        default="/run/user/1000/gvfs/smb-share:server=192.168.1.12,share=e/zzzProjekty/labels yolo/all",
                        help='path to the directory containing dataset')
    parser.add_argument('-port', '--PORT', type=int, default=8082, help='specified port (default - 8082)')
    parser.add_argument('-token', '--TOKEN', type=str, default=TOKEN, help='only: a-z0-9')
    options = parser.parse_args()
    return options


if __name__ == '__main__':
    args = parse_options()
    print(merge(**vars(args)))
