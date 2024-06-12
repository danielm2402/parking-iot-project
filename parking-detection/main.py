import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
from matplotlib import pyplot as plt
import cv2 as cv
from ultralytics import YOLO

model = YOLO('yolov8n.pt')

results = model.train(data='config.yaml', epochs=20, imgsz=640)


