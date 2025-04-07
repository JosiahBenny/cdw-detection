from ultralytics import solutions

inf = solutions.Inference(
    model="best.pt",
)
inf.inference()
