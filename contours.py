import numpy as np
import cv2 as cv

img = cv.imread('gsd1.jpg')
blank = np.zeros(img.shape, dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('doggy',gray)

blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
# cv.imshow('blur', blur)

canny = cv.Canny(blur, 100, 100)
cv.imshow('edge',canny)
  
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) #if intensity is below threshold, it is black, if above it is white  
# cv.imshow('threshold',thresh)

countours, heirarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE) 
#retr selects contours to show, next parameter approximates contours
#contours is a list of coordinates of contours
print (len(countours))

cv.drawContours(blank,countours, -1, (0,0,255), 1)
cv.imshow('cont', blank) 

cv.waitKey(0)
cv.destroyAllWindows()