# import onnxruntime
# help(onnxruntime)

from yolov5.detect import run

import torch
from redisai import Client as rai
import numpy as np
import cv2

# Connect to Redis
redis_client = rai(host='localhost', port=6379)
# redis_client.loadbackend('TORCH', '../RedisAI/build/backends/redisai_torch/redisai_torch.so')

# Load the ONNX model into RedisAI
model_path = 'yolov5/runs/train/results_15/weights/best.torchscript'
model_name = 'car_inspection'

# script_module = torch.jit.load(model_path)

with open(model_path, 'rb') as f:
    model = f.read()

redis_client.modelstore(model_name, 'torch', 'CPU', model)

# Generate sample input data
input_data = np.random.rand(1, 3, 224, 224).astype(np.float32)

print(input_data.shape)

cap = cv2.VideoCapture(0)
while cap.isOpened():
    return_, frame = cap.read()
    frame = frame.squeeze()
    print(frame.shape)
    break
    # results = model(frame)
#
#     input_tensor_name = 'input'
#     redis_client.tensorset(input_tensor_name, 'STRING', frame)
#
#
#
#     # Store the input tensor data
#     input_tensor_name = 'input'
#     redis_client.tensorset(input_tensor_name, 'STRING', frame)
#
#     # Run inference on the ONNX model
#     output_tensor_name = 'output'
#     redis_client.modelexecute(model_name, [input_tensor_name], [output_tensor_name])
#
#     # Get the inference results from RedisAI
#     output_tensor = redis_client.tensorget(output_tensor_name)
#     output_data = np.array(output_tensor)
#
#
#     print(output_data)



# Process and use inference data


# Clean up: Unload the model and delete the input/output tensors
redis_client.modeldel(model_name)
redis_client.tensordel(input_tensor_name)
redis_client.tensordel(output_tensor_name)






# run(weights='yolov5/runs/train/results_15/weights/best.onnx',
#     source='0',
#     # imgsz=(1280, 800),
#     # conf_thres=0.90,
#     device='cpu',
#     # iou_thres=0.95,
#     max_det=5,
#     save_crop=False,
#     )





"""
...
- Ograniczyć ilość robionych zdjęć
- Zwiekszyć rozdzielczość robionych zdjęć | zmienić rozdzielczość podczas treningu
- Apka w cloud czy on-device (edge)
- RedisAI, Torchscript, ONNX? | RedisAI
- Ustalić jakie rozszerzenie | .onnx
- Jak z dokerem, jak przenieść | RedisAI docker image
- Front apki (django startapp)
- Jak zapisać zdjęcia | save_crop=True
- Jak wysłać
- Testować użyteczność




ONNX
Loading yolov5/runs/train/results_15/weights/best.onnx for ONNX Runtime inference...
requirements: YOLOv5 requirement "onnxruntime" not found, attempting AutoUpdate...
Collecting onnxruntime
  Downloading onnxruntime-1.15.0-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (5.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 5.9/5.9 MB 30.1 MB/s eta 0:00:00
Collecting coloredlogs (from onnxruntime)
  Downloading coloredlogs-15.0.1-py2.py3-none-any.whl (46 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 46.0/46.0 kB 22.6 MB/s eta 0:00:00
Collecting flatbuffers (from onnxruntime)
  Downloading flatbuffers-23.5.26-py2.py3-none-any.whl (26 kB)
Requirement already satisfied: numpy>=1.24.2 in /home/robb/Desktop/PROJEKTY/nn/.env/lib/python3.11/site-packages (from onnxruntime) (1.24.3)
Requirement already satisfied: packaging in /home/robb/Desktop/PROJEKTY/nn/.env/lib/python3.11/site-packages (from onnxruntime) (23.1)
Requirement already satisfied: protobuf in /home/robb/Desktop/PROJEKTY/nn/.env/lib/python3.11/site-packages (from onnxruntime) (3.20.3)
Requirement already satisfied: sympy in /home/robb/Desktop/PROJEKTY/nn/.env/lib/python3.11/site-packages (from onnxruntime) (1.11.1)
Collecting humanfriendly>=9.1 (from coloredlogs->onnxruntime)
  Downloading humanfriendly-10.0-py2.py3-none-any.whl (86 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 86.8/86.8 kB 45.4 MB/s eta 0:00:00
Requirement already satisfied: mpmath>=0.19 in /home/robb/Desktop/PROJEKTY/nn/.env/lib/python3.11/site-packages (from sympy->onnxruntime) (1.3.0)
Installing collected packages: flatbuffers, humanfriendly, coloredlogs, onnxruntime
Successfully installed coloredlogs-15.0.1 flatbuffers-23.5.26 humanfriendly-10.0 onnxruntime-1.15.0

requirements: 1 package updated per ('onnx', 'onnxruntime')
requirements: ⚠️ Restart runtime or rerun command for updates to take effect

1/1: 0...  Success (inf frames 640x480 at 30.00 FPS)

"""