import cv2
import math


def frame_capture(path):
    imagesFolder = "video_frames"
    video = cv2.VideoCapture(path)
    second = 0

    frameRate = video.get(5)  # frame rate
    while(video.isOpened()):
        frameId = video.get(1)  # current frame number
        success, image = video.read()
        if (success != True):
            return success
        if (frameId % math.floor(frameRate) == 0):
            filename = imagesFolder + "/" + str(second) + ".jpg"
            cv2.imwrite(filename, image)
            second += 1
    video.release()


if __name__ == '__main__':

    frame_capture('test.mp4')
