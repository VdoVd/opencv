import cv2 as cv

img=cv.imread('photos/king.jpg')

cv.imshow('king',img)

def rescaleFrame(frame,scale=0.75):
    width=int(frame.shape[1]*scale)
    height=int(frame.shape)
cv.waitKey(0)

# capture=cv.VideoCapture('videos/1.mp4')

# while True:
#     isTrue,frame=capture.read()
#     cv.imshow('video',frame)

#     if cv.waitKey(20)&0xff==ord('d'):
#         break

# capture.release()
# cv.destroyAllWindows()