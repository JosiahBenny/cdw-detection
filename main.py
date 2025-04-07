from ultralytics import solutions

inf = solutions.Inference(
    model="C:/Users/USER/Documents/cdw/yolo models/yolov8s_100ep/detect/train\weights/best.pt",
)
inf.inference()