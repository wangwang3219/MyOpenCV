import cv2
import numpy as np
import os

flatNumpyArray = np.array(bytearray(os.urandom(120000)))
grayImage = flatNumpyArray.reshape(300,400)
cv2.imwrite('RandomGray.png',grayImage)
bgrImage = flatNumpyArray.reshape(100,400,3)
cv2.imwrite('RandomColor.png',bgrImage)

