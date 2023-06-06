import torch
import os
import time
import numpy as np
import cv2
from pathlib import Path


model = torch.hub.load('./yolov5', 'custom', path='yolov5/runs/train/results_11/weights/best.pt', source='local')

cap = cv2.VideoCapture(0)

while cap.isOpened():
    return_, frame = cap.read()

    results = model(frame)

    cv2.imshow('YOLO', np.squeeze(results.render()))
    # cv2.imshow('YOLO', frame)

    if cv2.waitKey(10) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

