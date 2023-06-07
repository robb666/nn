import torch
import os
import time
import numpy as np
import cv2
from pathlib import Path
import sys
import subprocess
from yolov5.detect import run


run(weights='yolov5/runs/train/results_14/weights/best.pt',
    source='0',
    conf_thres=0.50,
    device='cpu',
    iou_thres=0.95,
    max_det=4,
    save_crop=True,
    )

