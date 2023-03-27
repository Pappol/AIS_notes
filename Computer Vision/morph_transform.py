import cv2
import numpy as np
import sys
import matplotlib.pyplot as plt

def show_2_images(img1, lable1, img2, lable2):
    plt.subplot(121), plt.imshow(img1,cmap="gray"), plt.title(lable1)
    plt.subplot(122), plt.imshow(img2, cmap="gray"), plt.title(lable2)
    plt.show()

img = cv2.imread(c, cv2.IMREAD_GRAYSCALE)

assert img is not None, "could not read"

kernel = np.ones((5,5),np.uint8)

#perform erosion operation
erosion = cv2.erode(img, kernel, iterations=1)

#plot original and erosion side by side
#show_2_images(img, "original", erosion, "erosion")

dilation = cv2.dilate(img, kernel, iterations=2)
#show_2_images(img, "original", dilation, "dilation")


img = cv2.imread('Lab1/material/opening.png', cv2.IMREAD_GRAYSCALE)

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
#show_2_images(img, "original", opening, "opening")

img = cv2.imread('Lab1/material/closing.png', cv2.IMREAD_GRAYSCALE)

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
show_2_images(img, "original", closing, "closing")
