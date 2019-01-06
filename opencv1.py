import numpy as np
import cv2
img = np.zeros((3,3),dtype = np.uint8)
print(img, type(img), img.shape)
print("-------------------------------------")
img = cv2.cvtColor(img, cv2.COLOR_GRAY2BGR)
print(img, img.shape)
print("-------------------------------------")
img = cv2.imread('E:/OpenCv exercise/a.jpg')
cv2.imwrite('E:/OpenCv exercise/a.png', img)
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()