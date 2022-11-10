import cv2

cam = cv2.VideoCapture(0)

while cam.isOpened():
    status, image= cam.read()
    if status:
        cv2.imshow("live Camera", image)
        if cv2.waitKey(1) == 27:
            break
cam.release()
cv2.destroyAllWindows

