import cv2
import numpy as np
from numpy import *
import time
cap = cv2.VideoCapture(0)

pos_frame = 0
flag,frame = cap.read()
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
flags = 0
while(1):

    # Take each frame
    flag,frame = cap.read()
#    time.sleep(0.1)
    # Convert BGR to HSV
    prev_gray = gray.copy()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    flow = gray.copy() 
    flow =cv2.calcOpticalFlowFarneback(prev_gray,gray,flow,0.5,1,3,15,3,5,1)

    cv2.imshow('frame',frame)
    cv2.imshow('gray',gray)
    cv2.imshow('flow',flow)
#    cv2.imshow('res',res)
    k = cv2.waitKey(100) & 0xFF
#    k = cv2.waitKey(10) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
