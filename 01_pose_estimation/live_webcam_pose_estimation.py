import torch
from torchvision import transforms

from utils.datasets import letterbox
from utils.general import non_max_suppression_kpt
from utils.plots import output_to_keypoint, plot_skeleton_kpts

from models.experimental import attempt_load

import matplotlib.pyplot as plt
import cv2
import numpy as np

import time

import torch
import math

device = "cpu"

def load_model():
    try:
        model = attempt_load('model_weights/yolov7-w6-pose.pt', map_location=device)
        model.eval()
        print("Model loaded successfully")
        return model
    except:
        print("Model not found")

def predict(image, model):
    with torch.inference_mode():
        pred = model(image[None], augment=False)[0]

    prediction = non_max_suppression_kpt(pred, 0.25, 0.65, nc=model.yaml['nc'], nkpt=model.yaml['nkpt'], kpt_label=True)
    prediction = output_to_keypoint(prediction)

    if len(prediction) > 0:
        prediction = prediction[:, 7:]
        return prediction
    else:
        return None

def prepare_image(frame, image_size=640):
    image = np.asarray(frame)

    original_height, original_width = image.shape[:2]
    image = cv2.resize(image, (image_size, image_size))

    image_pt = torch.from_numpy(image).permute(2, 0, 1).to(device)
    image_pt = image_pt.float() / 255.0

    return image_pt, original_height, original_width

def resize_pose_estimation_prediction_output(prediction, original_height, original_width, image_size=640):
    prediction[:, 0::3] *= original_width / image_size
    prediction[:, 1::3] *= original_height / image_size

    return prediction

def plot_pose(prediction, image):
    image = np.asarray(image)

    for pred in range(prediction.shape[0]):
        plot_skeleton_kpts(image, prediction[pred].T, 3)

    return image

def detect_poses(frame, model):
    image, original_height, original_width = prepare_image(frame)
    prediction = predict(image, model)
    if prediction is not None:
        prediction = resize_pose_estimation_prediction_output(prediction, original_height, original_width)
        image_with_poses = plot_pose(prediction, frame)
        return image_with_poses
    else:
        return frame

pose_estimation_model = load_model()

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if ret:
        frame = detect_poses(frame, pose_estimation_model)
        cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()