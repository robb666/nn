import torch
import torchvision.transforms as transforms
from PIL import Image
import os
from pathlib import Path
import glob
import time


data_path = Path('/home/robb/Desktop/labels yolo')

image_path = data_path / 'zegary/3847fc_mv2.webp'


# Load the image
image = Image.open(image_path)

# Resize using PyTorch
resize_transform = transforms.Resize((224, 224))
resized_image = resize_transform(image)
print(type(resized_image))

# Convert to tensor
tensor_image = transforms.ToTensor()(resized_image)

print(tensor_image.shape)

save_path = Path('/home/robb/Desktop/resized.jpg')
resized_image.save(save_path)



# with open(save_path, 'wb') as f:
#     f.write(resized_image)



