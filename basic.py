import cv2 as cv

img = cv.imread('photos/park.jpg')
cv.imshow('bosto',img)

# converting to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#blur
blur = cv.GaussianBlur(img,(3,3),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

canny = cv.Canny(blur ,125 ,175)
cv.imshow('Canny Edges',canny)

dilated = cv.dilate(canny,(7,7),iterations=3)
cv.imshow('dilated',dilated)

eroded = cv.erode(dilated,(3,3),iterations=1)
cv.imshow('eroded',eroded)

cropped = img[50:200,200:400]
cv.waitKey(0)