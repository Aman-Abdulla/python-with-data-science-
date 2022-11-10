import cv2

cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_COMPLEX
color_black = (0,0,0)  #black
color_white = (255,255,255)  #white


while cam.isOpened():
    status, image= cam.read()
    if status:
        # add text
        cv2.putText(image,"Live Camera Feed",(10,30), font,1, color_black,2)
        cv2.imshow("live Camera", image)
        if cv2.waitKey(1) == 27: # 27 is the ASCII code of ESCAPE KEY
            break
cam.release()
cv2.destroyAllWindows

