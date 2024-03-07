import cv2 as CV
import numpy as np

image = CV.imread('Photos/Cat2.png')
#resize=CV.resize(image,(800,800))

#print( image.shape)

#Blur and gray image
#gray= CV.cvtColor(image, CV.COLOR_BGR2GRAY)


#IMG_BLUR= CV.GaussianBlur(gray,(9,9),0)`vhuh;l`

#CV.imwrite("blur.jpg", IMG_BLUR)

#CV.imshow("thres_image",IMG_BLUR)

#CV.imshow("gray_image",gray)

#In (2) RED, GREEN and Blue
while(1):
    #Take each frame
    frame = image
    
    #convert BGR to HSV
    hsv =CV.cvtColor(frame, CV.COLOR_BGR2HSV)
    
    #define range of blue color in HSV
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])
    
    #threshold the HSV image to get only blue colors
    mask = CV.inRange(hsv,lower_blue, upper_blue)
    
    #Bitwise-AND mask and orginal image
    res =CV.bitwise_and(frame, frame, mask= mask)
    
    CV.imshow('frame', frame)
    CV.imshow('mask', mask)
    CV.imshow('res', res)
    k = CV.waitKey(5) & 0XFF
    if k ==27:
      break
CV.destroyAllWindows()
