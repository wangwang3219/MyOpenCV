import cv2 as cv
import numpy as np


def extrace_object():
    capture = cv.VideoCapture("E:/OpenCV/Data/video/inRange.mp4")
    while(True):
        ret, frame = capture.read()
        if ret == False:
            break
        cv.imshow("video", frame)
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_hsv = np.array([0, 0, 0])
        upper_hsv = np.array([180, 255, 46])
        mask = cv.inRange(hsv, lowerb=lower_hsv, upperb=upper_hsv)
        cv.imshow("mask", mask)
        c = cv.waitKey(40)
        if c == 27:
            break

if __name__ == '__main__':
    extrace_object()
