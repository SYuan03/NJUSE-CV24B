import os

import cv2

image_color = cv2.imread('./I0.jpg')
image_gray = cv2.cvtColor(image_color, cv2.COLOR_BGR2GRAY)
os.makedirs("Q1_output", exist_ok=True)
cv2.imwrite('Q1_output/I1.jpg', image_gray)
