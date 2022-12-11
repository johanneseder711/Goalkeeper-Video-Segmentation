import torch
from torchvision import transforms

from utils.datasets import letterbox
from utils.general import non_max_suppression_kpt
from utils.plots import output_to_keypoint, plot_skeleton_kpts

import matplotlib.pyplot as plt
import cv2
import numpy as np

import time

import torch
import math

def load_model():
    #device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
    device = torch.device("cpu")
    model = torch.load('yolov7-w6-pose.pt', map_location=device)['model']
    # Put in inference mode
    model.float().eval()
    return model

model = load_model()

def run_inference(frame, model):
    # Resize and pad frame
    frame = letterbox(frame, 960, stride=64, auto=True)[0] # shape: (768, 960, 3)
    # Apply transforms
    frame = transforms.ToTensor()(frame) # torch.Size([3, 768, 960])
    # Turn frame into batch
    frame = frame.unsqueeze(0) # torch.Size([1, 3, 768, 960])
    output, _ = model(frame) # torch.Size([1, 45900, 57])
    return output, frame

def show_pose_estimated_video(output, image):
    output = non_max_suppression_kpt(output, 
                                     0.25, # Confidence Threshold
                                     0.65, # IoU Threshold
                                     nc=model.yaml['nc'], # Number of Classes
                                     nkpt=model.yaml['nkpt'], # Number of Keypoints
                                     kpt_label=True)
    with torch.no_grad():
        output = output_to_keypoint(output)
    nimg = image[0].permute(1, 2, 0) * 255
    nimg = nimg.cpu().numpy().astype(np.uint8)
    nimg = cv2.cvtColor(nimg, cv2.COLOR_RGB2BGR)
    
    for idx in range(output.shape[0]):
        plot_skeleton_kpts(nimg, output[idx, 7:].T, 3)
    
    cv2.imshow('frame', nimg)


# define a video capture object
vid = cv2.VideoCapture(0)
cv2.startWindowThread()

counter = 1 
while(True):
	
	# Capture the video frame
	# by frame
    ret, frame = vid.read()
    
    # take a picture approx. every sec
    if ret and counter%60==0:
        output, image = run_inference(frame, model)
        show_pose_estimated_video(output, image)
        
    counter = counter + 1
	# the 'q' button is set as the
	# quitting button you may use any
	# desired button of your choice
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()