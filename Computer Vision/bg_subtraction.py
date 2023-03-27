import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt

#define variables
LEARING_RATE = -1
HISTORY = 200
N_MIXTURES = 200
BACKGROUND_RATIO = 0.7
NOISE_SIGMA = 1
MOG_VERSION = 1



#import video
cap = cv2.VideoCapture('Lab1/material/video.mp4')

if not cap.isOpened():
    sys.exit("Could not read the video.")

if MOG_VERSION == 1:
    fgbg = cv2.bgsegm.createBackgroundSubtractorMOG(HISTORY, N_MIXTURES, BACKGROUND_RATIO, NOISE_SIGMA)
else:
    fgbg = cv2.createBackgroundSubtractorMOG2()

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    #apply background subtraction
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    fgmask = fgbg.apply(gray, LEARING_RATE)
    #get background
    if MOG_VERSION == 2:
        background = fgbg.getBackgroundImage()
        #show background
        cv2.imshow('background', background)
    cv2.imshow('frame', fgmask)
    if cv2.waitKey(1) == ord('q'):
        break