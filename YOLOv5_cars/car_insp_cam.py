from yolov5.detect import run


run(weights='yolov5/runs/train/results_15/weights/best.pt',
    source='0',
    conf_thres=0.90,
    device='cpu',
    iou_thres=0.95,
    max_det=5,
    save_crop=False,
    )


