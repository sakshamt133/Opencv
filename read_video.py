import cv2 as cv


def read_video(path):

    video = cv.VideoCapture(path)
    check = True

    while check:
        check, frame = video.read()

        cv.imshow("Video", frame)

        if cv.waitKey(20) and 0xff == ord('d'):
            break
