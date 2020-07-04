import tensorflow as tf
import cv2 
import matplotlib.pyplot as plt
import random
from tensorflow import keras
from tensorflow.keras import layers
import numpy as np
import gc
import os
import glob
import math
import time
AUTO = tf.data.experimental.AUTOTUNE
from create_dataset_utils import *
from adap_conv_model_utils import *
import adap_conv_model_config as config

model=create_model()

#Specify weights file name here
checkpoint_name=config.CHECKPOINT_NAME
checkpoint_path=config.CHECKPOINT_PATH
model.load_weights(checkpoint_path+checkpoint_name)

#Specify file paths of two frames and interpolated frame path here 
video_path=config.VIDEO_PATH
video_name=config.VIDEO_NAME
interpolated_video_path=config.INTERPOLATED_VIDEO_PATH

cap=cv2.VideoCapture(video_path+video_name)
fourcc=cap.get(cv2.CAP_PROP_FOURCC)
fps=(cap.get(cv2.CAP_PROP_FPS))
height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)
video=cv2.VideoWriter(filename=(interpolated_video_path+video_name[:-4]+'_IP'+video_name[-4:]),fourcc=fourcc,fps=fps*2,frameSize=(height,width))
# print(fourcc,fps,height,width)
predict_video(model,cap,video,save_orignal_video=True)
cap.release()
video.release()
print("Success")