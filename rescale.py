import cv2 as cv

# img=cv.imread('photos/king.jpg')

# cv.imshow('king',img)

def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape[0]*scale)
    dimensions=(width,height)
    return cv.resize(frame,dimensions,interpolation=cv.INTER_AREA)



capture=cv.VideoCapture('videos/1.mp4')

while True:
    isTrue,frame=capture.read()
    
    frame_resized = rescaleFrame(frame,.5)

    cv.imshow('video',frame)
    cv.imshow('video resize',frame_resized)
    if cv.waitKey(20)&0xff==ord('d'):
        break

capture.release()

cv.destroyAllWindows()
cv.waitKey(0)