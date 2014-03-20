import cv2
import numpy as np
import time
cap = cv2.VideoCapture(0)

pos_frame = 0
while(1):

    # Take each frame
    flag,frame = cap.read()
#    time.sleep(0.1)
    # Convert BGR to HSV
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    kernel1 = np.ones((5,5),np.float32)/25
    kernel2 = np.ones((10,10),np.float32)/100
    kernel3 = np.ones((5,5),np.float32)/100
    fblur1 = cv2.filter2D(gray,-1,kernel1)
    fblur2 = cv2.filter2D(gray,-1,kernel2)
    fblur3 = cv2.filter2D(gray,-1,kernel3)

    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    cv2.imshow('blur1',fblur1)
    cv2.imshow('blur2',fblur2)
    cv2.imshow('blur3',fblur3)
#    cv2.imshow('res',res)
    k = cv2.waitKey(100) & 0xFF
#    k = cv2.waitKey(10) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
