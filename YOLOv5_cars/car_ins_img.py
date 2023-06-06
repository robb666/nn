import os
import glob
import matplotlib.pyplot as plt
import cv2
import requests
import wandb
import random
import numpy as np
import zipfile
import sys
import subprocess


SEED = 42
np.random.seed(SEED)

TRAIN = False
EPOCHS = 50


def download_file(url, save_name):
    url = url
    if not os.path.exists(save_name):
        file = requests.get(url)
        open(save_name, 'wb').write(file.content)
    else:
        print('File already present, skipping download...')


class_names = ['Dowód rej.', 'Kuczyk(i)', 'Lewy przód', 'Numer rej.', 'Prawy tył', 'Przebieg', 'VIN', 'Wnętrze']
colors = np.random.uniform(0, 255, size=(len(class_names), 3))


def yolo2bbox(bboxes):
    xmin, ymin = bboxes[0] - bboxes[2] / 2, bboxes[1] - bboxes[3] / 2
    xmax, ymax = bboxes[0] + bboxes[2] / 2, bboxes[1] + bboxes[3] / 2
    return xmin, ymin, xmax, ymax


def plot_box(image, bboxes, labels):
    # Need the image height and width to denormalize the
    # bounding box
    h, w, _ = image.shape
    for box_num, box in enumerate(bboxes):
        x1, y1, x2, y2 = yolo2bbox(box)
        # denormalize the coordinates
        xmin = int(x1*w)
        ymin = int(y1*h)
        xmax = int(x2*w)
        ymax = int(y2*h)
        width = xmax - xmin
        height = ymax - ymin

        class_name = class_names[int(labels[box_num])]

        cv2.rectangle(
            image,
            (xmin, ymin), (xmax, ymax),
            color=colors[class_names.index(class_name)],
            thickness=2
        )

        font_scale = min(1, max(3, int(w/500)))
        font_thickness = min(2, max(10, int(w/50)))

        p1, p2 = (int(xmin), int(ymin)), (int(xmax), int(ymax))
        # Text width and height
        tw, th = cv2.getTextSize(
            class_name,
            0, fontScale=font_scale, thickness=font_thickness
        )[0]
        p2 = p1[0] + tw, p1[1] + -th -10
        cv2.rectangle(
            image,
            p1, p2,
            color=colors[class_names.index(class_name)],
            thickness=-1,
        )
        cv2.putText(
            image,
            class_name,
            (xmin+1, ymin-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            font_scale,
            (225, 225, 225),
            font_thickness
        )
    return image


# Function to plot images with the bounding boxes
def plot(image_paths, label_paths, num_samples):
    print(os.getcwd())
    os.chdir('./dataset')
    all_training_images = glob.glob(image_paths)
    all_training_labels = glob.glob(label_paths)
    all_training_images.sort()
    all_training_labels.sort()

    num_images = len(all_training_images)

    plt.figure(figsize=(15, 12))
    for i in range(num_samples):
        j = random.randint(0, num_images-1)
        image = cv2.imread(all_training_images[j])
        with open(all_training_labels[j], 'r') as f:
            bboxes = []
            labels = []
            label_lines = f.readlines()
            for label_line in label_lines:
                label = label_line[0]
                bbox_string = label_line[2:]

                x_c, y_c, w, h = bbox_string.split(' ')
                x_c = float(x_c)
                y_c = float(y_c)
                w = float(w)
                h = float(h)
                bboxes.append([x_c, y_c, w, h])
                labels.append(label)
        result_image = plot_box(image, bboxes, labels)
        plt.subplot(2, 2, i+1)
        plt.imshow(result_image[:, :, ::-1])
        plt.axis('off')
    plt.subplots_adjust(wspace=0)
    plt.tight_layout()
    plt.show()


def set_results_dir():
    # Directory to store results
    res_dir_count = len(glob.glob('runs/train/*'))
    print(f'Current number of results directories: {res_dir_count}')
    if TRAIN:
        RES_DIR = f'results_{res_dir_count + 1}'
        print(RES_DIR)
    else:
        RES_DIR = f'results_{res_dir_count}'
    return RES_DIR


def monitor_wandb():
    wandb.init(
        project='YOLOv5 Cars'
    )


# def monitor_tensorboard():
    # import tensorflow as tf
    # # subprocess.run('tensorboard')
    # # %load_ext tensorboard
    # subprocess.run(['tensorboard', '--logdir', 'runs/train'])
    # # %tensorboard --logdir runs/train


# Clone YOLOv5 repo
if not os.path.exists('yolov5'):
    print('Cloning YOLOv5...')
    subprocess.run(['git', 'clone', 'https://github.com/ultralytics/yolov5.git'])


# plot(image_paths='train/images/*',
#      label_paths='train/labels/*',
#      num_samples=4)


# monitor_wandb()

print(os.getcwd())
os.chdir('./yolov5')

RES_DIR = set_results_dir()

if TRAIN:
    subprocess.run(['python', 'train.py', '--data', '../dataset/data.yaml', '--weights', 'yolov5s.pt',
                    '--img', '640', '--epochs', f'{EPOCHS}', '--batch-size', '16', '--name', f'{RES_DIR}'])

# --freeze 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14


def show_valid_results(RES_DIR):
    subprocess.run(['ls', f'runs/train/{RES_DIR}'])
    EXP_PATH = f'runs/train/{RES_DIR}'
    validation_pred_images = glob.glob(f'{EXP_PATH}/*_pred.jpg')
    print(validation_pred_images)
    for pred_image in validation_pred_images:
        image = cv2.imread(pred_image)
        plt.figure(figsize=(19, 16))
        plt.imshow(image[:, :, ::-1])
        plt.axis('off')
        plt.show()


def inference(RES_DIR, data_path):
    infer_dir_count = len(glob.glob('runs/detect/*'))
    print(f'Current number of inference detection directories: {infer_dir_count}')
    INFER_DIR = f'inference_{infer_dir_count + 1}'
    print(INFER_DIR)
    # Inference on images.
    subprocess.run([sys.executable, 'detect.py', '--weights', f'runs/train/{RES_DIR}/weights/best.pt',
                    '--source', f'{data_path}', '--name', f'{INFER_DIR}'])
    return INFER_DIR


rnd_array = np.random.randint(0, 50, size=10)


def visualize(INFER_DIR):
    INFER_PATH = f'runs/detect/{INFER_DIR}'
    infer_images = glob.glob(f'{INFER_PATH}/*.jpg')
    for i, pred_image in enumerate(infer_images):
        if i == 4:
            break
        image = cv2.imread(infer_images[rnd_array[i]])
        plt.figure(figsize=(12, 9))
        plt.imshow(image[:, :, ::-1])
        plt.axis('off')
        plt.show()


show_valid_results(RES_DIR)


# inference(RES_DIR, '/home/robb/Desktop/PROJEKTY/nn/YOLOv5_cars/dataset/valid/check')

wandb.finish()









# import wandb
# import random
#
# # start a new wandb run to track this script
# wandb.init(
#     # set the wandb project where this run will be logged
#     project="my-awesome-project",
#
#     # track hyperparameters and run metadata
#     config={
#         "learning_rate": 0.02,
#         "architecture": "CNN",
#         "dataset": "CIFAR-100",
#         "epochs": 10,
#     }
# )
#
# # simulate training
# epochs = 10
# offset = random.random() / 5
# for epoch in range(2, epochs):
#     acc = 1 - 2 ** -epoch - random.random() / epoch - offset
#     loss = 2 ** -epoch + random.random() / epoch + offset
#
#     # log metrics to wandb
#     wandb.log({"acc": acc, "loss": loss})
#
# # [optional] finish the wandb run, necessary in notebooks
# wandb.finish()