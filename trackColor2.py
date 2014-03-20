import cv2
import numpy as np

flag = 1
capture = cv2.VideoCapture(0)

while True:
      _,img = capture.read()
      simg = cv2.blur(img, (5,5))
      simg = cv2.GaussianBlur(simg,(5,5),0)
      simg = cv2.medianBlur(simg,5)

      frame1 = cv2.rectangle(simg,(300,100),(400,500),(0,255,0))
      frame2 = simg[100:500,300:400]

      hsv = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)

      # define range of blue color in HSV
      lower_yellow = np.array([20,100,100])
      upper_yellow = np.array([30,255,255])

      # Threshold the HSV image to get only yellow colors
      mask = cv2.inRange(hsv, lower_yellow, upper_yellow)

      contours,hierarchy = cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
      cv2.drawContours(mask,contours,-1,(0,255,0))

      img_mom = cv2.moments(mask,0)
      area = img_mom['m00']

      if((area > 500000) and flag==1):
        print 'found'
        flag=0
        print area




      cv2.imshow('2',simg)
      cv2.imshow('area',frame2)
      cv2.imshow('3',mask)
      k = cv2.waitKey(20) & 0xFF
      if k == 27:
          break


cv2.destroyAllWindows()
