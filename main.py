import cv2 as cv
import numpy as np
from matplotlib import pyplot as pt
filename = 'chessboard.png'
img = cv.imread(filename)
print("2323")
img= cv.resize(img,(300,300),interpolation = cv.INTER_AREA)
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
gray = np.float32(gray)
dst = cv.cornerHarris(gray,2,3,0.04)
print(dst)
#result is dilated for marking the corners, not important
dst = cv.dilate(dst,None)
print(dst)
# Threshold for an optimal value, it may vary depending on the image.
img[dst>0.01*dst.max()]=[0,0,255]
x=140
y=140
# cv.circle(img,(150,111),10,(255,0,0),0)


pt.imshow(img)
pt.show()
print(img.shape)
if cv.waitKey(0) & 0xff == 27:
    cv.destroyAllWindows()
