from redisai import Client as rai
import numpy as np
import cv2

model_path = 'yolov5/runs/train/results_15/weights/best.torchscript'

# Connect to Redis
redis_client = rai(host='localhost', port=6379)

img = '/home/robb/Desktop/PROJEKTY/nn/YOLOv5_cars/yolov5/data/images/bus.jpg'
img = cv2.imread(img)
print(img)
img = np.transpose(img, (2, 0, 1))
print(img)
img = img[None, :].astype(np.float32) / 255.0  # adds batch size (1, 3, 1080, 810)
print(img)

with open(model_path, 'rb') as f:
    model = f.read()


redis_client.modelstore('willitwork', 'torch', 'CPU', model)

redis_client.tensorset('my_tensor', img)

redis_client.modelexecute('willitwork', ['my_tensor'], ['output'])

output_tensor = redis_client.tensorget('output')
output_data = np.array(output_tensor)



# redis_client.tensorset(key='my_tensor', shape=[2, 2], tensor=[1, 2, 3, 4], dtype='float')
#
# getget = redis_client.tensorget(key='my_tensor', as_numpy=False, meta_only=False)
# print(getget)
