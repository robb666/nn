from redisai import Client as rai
import numpy as np
import cv2


# Connect to Redis
redis_client = rai(host='localhost', port=6379)
print(redis_client)

redis_client.tensorset(key='my_tensor', shape=[2, 2], tensor=[1, 2, 3, 4], dtype='float')

getget = redis_client.tensorget(key='my_tensor', as_numpy=False, meta_only=False)
print(getget)
