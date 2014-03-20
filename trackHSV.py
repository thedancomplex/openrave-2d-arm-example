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
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110, 50, 50], dtype=np.uint8)
    upper_blue = np.array([130,255,255], dtype=np.uint8)

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Erode/dilate
    kernelerd = np.ones((3,3),np.uint8)
    kerneldil = np.ones((5,5),np.uint8)
    kernel = np.ones((2,2),np.uint8)
    erd = cv2.erode(mask,kernelerd,iterations = 2)
    dil = cv2.dilate(erd,kerneldil,iterations = 2)

    # Get Center
    try:
      M = cv2.moments(dil)
      cx = int(M['m10']/M['m00'])
      cy = int(M['m01']/M['m00'])
     # (x,y),radius = cv2.minEnclosingCircle(dil)
      center = (cx,cy)
      radius = int(10)
      cv2.circle(frame,center,radius, (0,0,255), -1)
      #cv2.circle(frame,center,radius,(0,255,0),2)
      #ellipse = cv2.fitEllipse(dil)
      #cv2.ellipse(frame,ellipse,(0,255,0),2)
    except:
      print 'No Tracking'

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('eroded',erd)
    cv2.imshow('dilate',dil)
    k = cv2.waitKey(200) & 0xFF
#    k = cv2.waitKey(10) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
