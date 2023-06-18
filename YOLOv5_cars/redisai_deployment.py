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


# # Clean up: Unload the model and delete the input/output tensors
# redis_client.modeldel(model_name)
# redis_client.tensordel(input_tensor_name)
# redis_client.tensordel(output_tensor_name)

