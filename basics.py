import cv2 as cv
import numpy as np

img = cv.imread('gsd1.jpg')
cv.imshow('doggy',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('doggy',gray)

average = cv.blur(img, (7,7))
# cv.imshow('avergae blur', average)

blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)#more natural
# cv.imshow('blur', blur)

median = cv.medianBlur(img, 1)
# cv.imshow ('median', median)

natural = cv.bilateralFilter(img, 7, 15, 15)
# cv.imshow('natural', natural)

canny = cv.Canny(gray, 100, 100)
cv.imshow('canny',canny)

lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))#pixel vals are converted to their absolute vals
cv.imshow('lap',lap)

sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
# cv.imshow('x',sobelx)
# cv.imshow('y',sobely)
combined = cv.bitwise_or(sobelx,sobely)
cv.imshow('comb',combined)

dilated = cv.dilate(canny, (10,10), iterations=3)
# cv.imshow('dilate',dilated)

eroded = cv.erode(dilated, (3,3), iterations=1)
# cv.imshow('eroded', eroded)

resize = cv.resize (img, (480, 360), interpolation=cv.INTER_NEAREST)
# cv.imshow('rezised', resize)

crop = img[50:200,200:400]
# cv.imshow('cropped',crop)

rotate = cv.rotate(img, 2, 1)
# cv.imshow('rotate',rotate)

cv.waitKey(0)
cv.destroyAllWindows()
