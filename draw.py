import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')

# cv.imshow('Blank',blank)

# # blank[200:300,300:400] = 0,0,255

# # cv.imshow('Green',blank)

# cv.rectangle(blank,(0,0),(blank.shape[1]//2,blank.shape[1]//2),(0,255,0),thickness=-1)
# # cv.imshow('Rect',blank)

# cv.circle(blank,(blank.shape[1]//2,blank.shape[1]//2),40,(0,0,255),thickness=-1)

# cv.imshow('circle',blank)

# cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=3)

# cv.imshow('Line',blank)

cv.putText(blank,'hello,my name is jason!!!',(225,225),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),2)

cv.imshow('text',blank)

cv.waitKey(0)