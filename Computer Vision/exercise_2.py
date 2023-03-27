import cv2
import numpy as np
import sys

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    sys.exit("Could not read the video.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    #flip video vertically
    frame = cv2.flip(frame, 0)
    
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
