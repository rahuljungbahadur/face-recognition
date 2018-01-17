"""
This script Captures the video through the webcam
and detects the faces in the video
author: Rahul
date: 28th Dec 2017
"""
import cv2, time

video = cv2.VideoCapture(0)
##cascade classifier
face = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
##
while True:    
    frame, image = video.read(0)
    
    print(frame)
    print(image)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    #cv2.imshow("video_capture", image)
    
    ##destroying windows
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    
    ###detecting faces
    
    
    faces = face.detectMultiScale(image_gray, scaleFactor = 1.05, minNeighbors = 5)
    
    #print(faces)
    for x, y, w, h in faces:
        image = cv2.rectangle(image, (x,y),((x+w), (y+h)), color = (0,0,255), thickness = 4)
    
    cv2.imshow("my_face", image)    
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break


###
#time.sleep(3)
#cv2.waitKey(0)
video.release()
cv2.destroyAllWindows()

# type(video)
# print(video)