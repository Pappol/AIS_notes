import cv2
import numpy as np
import sys

img = cv2.imread('Lab1/material/home.jpg')
if img is None:
    sys.exit("Could not read the image.") 

cv2.imshow("Display window", img)
k = cv2.waitKey(0)
if k == ord("s"):
    cv2.imwrite("Lab1/material/home_copy.jpg", img)

cv2.destroyAllWindows()
