import argparse
import numpy as np
import cv2

import redisai


def load_classes(path):
    # Loads *.names file at 'path'
    with open(path, 'r') as f:
        names = f.read().split('\n')
    return list(filter(None, names))  # filter removes empty strings (such as last line)


def letterbox_image(img, inp_dim):
    """resize image with unchanged aspect ratio using padding"""
    img_w, img_h = img.shape[1], img.shape[0]
    w, h = inp_dim
    new_w = int(img_w * min(w/img_w, h/img_h))
    new_h = int(img_h * min(w/img_w, h/img_h))
    resized_image = cv2.resize(img, (new_w,new_h), interpolation=cv2.INTER_LINEAR)

    canvas = np.full((inp_dim[1], inp_dim[0], 3), 128)

    canvas[(h-new_h)//2:(h-new_h)//2 + new_h,(w-new_w)//2:(w-new_w)//2 + new_w, :] = resized_image

    return canvas


def xywh2xyxy(x):
    # Transform box coordinates from [x, y, w, h] to [x1, y1, x2, y2] (where xy1=top-left, xy2=bottom-right)
    y = np.zeros_like(x)
    y[:, 0] = x[:, 0] - x[:, 2] / 2  # top left x
    y[:, 1] = x[:, 1] - x[:, 3] / 2  # top left y
    y[:, 2] = x[:, 0] + x[:, 2] / 2  # bottom right x
    y[:, 3] = x[:, 1] + x[:, 3] / 2  # bottom right y
    return y


def clip_coords(boxes, img_shape):
    # Clip bounding xyxy bounding boxes to image shape (height, width)
    boxes[:, 0] = np.clip(boxes[:, 0], 0, img_shape[1])  # x1
    boxes[:, 1] = np.clip(boxes[:, 1], 0, img_shape[0])  # y1
    boxes[:, 2] = np.clip(boxes[:, 2], 0, img_shape[1])  # x2
    boxes[:, 3] = np.clip(boxes[:, 3], 0, img_shape[0])  # y2


def scale_coords(img1_shape, coords, img0_shape, ratio_pad=None):
    # Rescale coords (xyxy) from img1_shape to img0_shape
    if ratio_pad is None:  # calculate from img0_shape
        gain = max(img1_shape) / max(img0_shape)  # gain  = old / new
        pad = (img1_shape[1] - img0_shape[1] * gain) / 2, (img1_shape[0] - img0_shape[0] * gain) / 2  # wh padding
    else:
        gain = ratio_pad[0][0]
        pad = ratio_pad[1]

    coords[:, [0, 2]] -= pad[0]  # x padding
    coords[:, [1, 3]] -= pad[1]  # y padding
    coords[:, :4] /= gain
    clip_coords(coords, img0_shape)
    return coords


def box_iou(box1, box2):
    # https://github.com/pytorch/vision/blob/master/torchvision/ops/boxes.py
    """
    Return intersection-over-union (Jaccard index) of boxes.
    Both sets of boxes are expected to be in (x1, y1, x2, y2) format.
    Arguments:
        box1 (Tensor[N, 4])
        box2 (Tensor[M, 4])
    Returns:
        iou (Tensor[N, M]): the NxM matrix containing the pairwise
            IoU values for every element in boxes1 and boxes2
    """

    def box_area(box):
        # box = 4xn
        return (box[2] - box[0]) * (box[3] - box[1])

    area1 = box_area(box1.transpose())
    area2 = box_area(box2.transpose())

    inter = (np.minimum(box1[:, None, 2:], box2[:, 2:]) - np.maximum(box1[:, None, :2], box2[:, :2])).clip(0).prod(2)
    return inter / (area1[:, None] + area2 - inter)  # iou = inter / (area1 + area2 - inter)


def non_max_suppression(prediction, conf_thres=0.1, iou_thres=0.6, classes=None):
    """
    Performs  Non-Maximum Suppression on inference results
    Returns detections with shape:
        nx6 (x1, y1, x2, y2, conf, cls)
    """

    # Box constraints
    min_wh, max_wh = 2, 4096  # (pixels) minimum and maximum box width and height

    nc = prediction.shape[1] - 5  # number of classes
    output = [None] * len(prediction)

    for xi, x in enumerate(prediction):  # image index, image inference
        # Apply conf constraint
        x = x[x[:, 4] > conf_thres]

        # Apply width-height constraint
        x = x[((x[:, 2:4] > min_wh) & (x[:, 2:4] < max_wh)).all(1)]

        # If none remain process next image
        if not x.shape[0]:
            continue

        # Compute conf
        x[..., 5:] *= x[..., 4:5]  # conf = obj_conf * cls_conf

        # Box (center x, center y, width, height) to (x1, y1, x2, y2)
        box = xywh2xyxy(x[:, :4])

        # Detections matrix nx6 (xyxy, conf, cls)
        conf = x[:, 5:].max(axis=1)
        j = x[:, 5:].argmax(axis=1)
        x = np.concatenate((box, conf[:, None], j.astype(np.float32)[:, None]), axis=1)

        # Filter by class
        if classes:
            x = x[(j.reshape(-1, 1) == np.array(classes)).any(1)]

        # Apply finite constraint
        if not np.isfinite(x).all():
            x = x[np.isfinite(x).all(1)]

        # If none remain process next image
        n = x.shape[0]  # number of boxes
        if not n:
            continue

        # Batched NMS
        c = x[:, 5]  # classes
        boxes, scores = x[:, :4].copy() + c.reshape(-1, 1) * max_wh, x[:, 4]  # boxes (offset by class), scores
        iou = np.triu(box_iou(boxes, boxes), k=1)  # upper triangular iou matrix
        i = iou.max(0, keepdims=True)[0] < iou_thres

        output[xi] = x[i]

    return output


def load_model(r, filename, device):

    with open(filename, 'rb') as f:
        model = f.read()

    r.modelset('yolo3', 'TORCH', device, model)


def predict(r, img, orig_shape, names):
    # Put channels first
    img = np.transpose(img, (2, 0, 1))

    # Add batch dimension of 1, convert to float32 and normalize
    img = img[None, :].astype(np.float32) / 255.0

    r.tensorset('in', img)
    r.modelrun('yolo3', ['in'], ['out'])
    pred = r.tensorget('out')

    pred = non_max_suppression(pred, opt.conf_thres, opt.iou_thres, opt.classes)

    for i, det in enumerate(pred):  # detections per image
        if det is not None and len(det):
            # Rescale boxes from img_size to im0 size
            det[:, :4] = scale_coords(img.shape[2:], det[:, :4], orig_shape).round()

            # Print results
            for *xyxy, conf, cls in det:
                print(names[int(cls)], conf, xyxy)


if __name__ == '__main__':

    model_path = 'yolov5/runs/train/results_15/weights/best.pt'
    model_name = 'car_inspection'

    parser = argparse.ArgumentParser()
    parser.add_argument('--cfg', type=str, default=model_path, help='*.cfg path')
    # parser.add_argument('--cfg', type=str, default='cfg/yolov3-spp.cfg', help='*.cfg path')
    parser.add_argument('--names', type=str, default='data/coco.names', help='*.names path')
    parser.add_argument('--model', type=str, default=model_path, help='traced model path')
    # parser.add_argument('--model', type=str, default='yolov3-spp-traced.pt', help='traced model path')
    parser.add_argument('--device', type=str, default='cpu', help='device to run inference on')
    parser.add_argument('--img-size', type=int, default=640, help='inference size (pixels)')
    parser.add_argument('--conf-thres', type=float, default=0.3, help='object confidence threshold')
    parser.add_argument('--iou-thres', type=float, default=0.6, help='IOU threshold for NMS')
    parser.add_argument('--classes', nargs='+', type=int, help='filter by class')
    parser.add_argument('--images', nargs='+', type=str, help='images')
    opt = parser.parse_args()
    print(opt)

    r = redisai.Client()

    load_model(r, opt.model, opt.device)

    names = load_classes(opt.names)

    for filename in opt.images:
        print('Processing', filename)
        img0 = cv2.imread(filename)
        img = letterbox_image(img0, (opt.img_size, opt.img_size))

        predict(r, img, img0.shape[:2], names)












# # Connect to Redis
# redis_client = rai(host='localhost', port=6379)
# print(redis_client)
#
# redis_client.tensorset(key='my_tensor', shape=[2, 2], tensor=[1, 2, 3, 4], dtype='float')
#
# getget = redis_client.tensorget(key='my_tensor', as_numpy=False, meta_only=False)
# print(getget)


