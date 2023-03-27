import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt

#open video
cap = cv2.VideoCapture('Lab1/material/video.mp4')

if not cap.isOpened():
    sys.exit("Could not read the video.")

frame_list = []
N=15
MAX_FRAMES = 1000
THRESHOLD = 50
MAXVAL = 255

for t in range(1000):
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    #flip video vertically
    frame_fgray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #save frames in a list
    frame_list.append(frame_fgray)
    
    #apply frame differencing
    
    if len(frame_list) > N:
        result = cv2.absdiff(frame_list[t-N], frame_list[t])
        #apply threshold
        ret, motion_mask = cv2.threshold(result, THRESHOLD, MAXVAL, cv2.THRESH_BINARY)

        cv2.imshow('original', frame)
        cv2.imshow('frame', motion_mask)
        if cv2.waitKey(1) == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
