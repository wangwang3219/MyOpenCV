import cv2
cliked = False


def onMouse(event, x, y, flags, param):
	global cliked
	if event == cv2.EVENT_LBUTTONUP:
		cliked = True


cameraCapture = cv2.VideoCapture(0)
cv2.namedWindow('My Window')
cv2.setMouseCallback('My Window', onMouse)
print('Showing')
success, frame = cameraCapture.read()
while success and cv2.waitKey(1) == -1 and not cliked:
	cv2.imshow('My Window', frame)
	success, frame = cameraCapture.read()
cv2.destroyWindow('My Window')
cameraCapture.release()
