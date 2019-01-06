import numpy as np
import cv2

#读取AVI文件的帧，并采用YUV颜色编码将其写入另一个帧中
# videoCapture = cv2.VideoCapture('E:/OpenCV exercise/1.avi')
# fps = videoCapture.get(cv2.CAP_PROP_FPS)
# size = (int(videoCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
# 		int(videoCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# videoWriter = cv2.VideoWriter('E:/OpenCV exercise/1.avi',cv2.VideoWriter_fourcc('I','4','2','0'),fps,size)
# success, frame = videoCapture.read()
# while success:
# 	videoWriter.write(frame)
# 	success, frame = videoCapture.read()


#录屏10秒
# cameraCapture = cv2.VideoCapture(0)
# fps = 30
# size = (int(cameraCapture.get(cv2.CAP_PROP_FRAME_WIDTH)),
# 		int(cameraCapture.get(cv2.CAP_PROP_FRAME_HEIGHT)))
# videoWriter = cv2.VideoWriter('E:/OpenCV exercise/2.avi',cv2.VideoWriter_fourcc('I','4','2','0'), fps, size)
# success, frame = cameraCapture.read()
# numFramesRemaining = 10 * fps - 1
# while success and numFramesRemaining > 0:
# 	videoWriter.write(frame)
# 	success, frame = cameraCapture.read()
# 	numFramesRemaining -= 1
# cameraCapture.release()


# cap = cv2.VideoCapture("E:/Opencv exercise/1.avi")
# while True:
#     # get a frame
#     ret, frame = cap.read()
#     # show a frame
#     cv2.imshow("capture", frame)
#     if cv2.waitKey(100) & 0xFF == ord('q'):
#         break
# cap.release()
# cv2.destroyAllWindows()


if __name__ == '__main__':
    # 打开视频
    reader = cv2.VideoCapture("E:/Opencv exercise/1.avi")
    print(reader.isOpened())
    # 视频的宽度
    width = int(reader.get(cv2.CAP_PROP_FRAME_WIDTH))
    # 视频的高度
    height = int(reader.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # 视频的帧率
    fps = reader.get(cv2.CAP_PROP_FPS)
    # 视频的编码
    fourcc = int(reader.get(cv2.CAP_PROP_FOURCC))

    have_more_frame = True
    while have_more_frame:
        have_more_frame, frame = reader.read()
        if have_more_frame:
            # 显示
            cv2.imshow("Video", frame)
            # 延时
            cv2.waitKey(24)
    reader.release()