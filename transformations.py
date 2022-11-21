import numpy as np
import cv2 as cv

img = cv.imread('photos/park.jpg')

cv.imshow('boston',img)

#transtation

def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

translated=translate(img,100,100)

cv.imshow('translate',translated)

def rotate(img,angle,roPoint=None):
    (height,width) = img.shape[:2]

    if roPoint is None:
        roPoint=(width//2,height//2)
    
    rotMat = cv.getRotationMatrix2D(roPoint,angle,1.0)
    dimensions = (width,height)

    return cv.warpAffine(img,rotMat,dimensions)
#rotate
# rotated = rotate(img,-45)
# cv.imshow('rotate',rotated)

# rotate_rotated = rotate(rotated,-45)
# cv.imshow('rotated',rotate_rotated)

# rotated_rotedd = rotate(rotate_rotated,-45)
# cv.imshow('rotated three',rotated_rotedd)

#resize
resize = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resize',resize)

#flip
flip = cv.flip(img,1)
cv.imshow('flip',flip)

#cropped
cropped = img[200:400,300:400]
cv.imshow('cropped',cropped)
cv.waitKey(0)