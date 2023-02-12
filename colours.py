import cv2 as cv
import numpy as np

img = cv.imread('gsd1.jpg')
cv.imshow('doggy',img)

blank = np.zeros(img.shape[:2], dtype='uint8')

# plt.imshow(img)
# plt.show()

b,g,r = cv.split(img)

# cv.imshow ('blue',b)
# cv.imshow ('green',g)
# cv.imshow ('red',r)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])
# cv.imshow('blue',blue)
# cv.imshow('green',green)
# cv.imshow('red',red)

# print(img.shape)
# print(b.shape)
# print(g.shape)
# print(r.shape)

merge = cv.merge([b,g,r])
# cv.imshow('merged colors', merge)


gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('gray doggy',gray)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
# cv.imshow('hsv doggy', hsv)

lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
# cv.imshow('lab dog', lab)

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# cv.imshow('rgb doggy', rgb)
# plt.imshow(rgb)
# plt.show()

cv.waitKey(0)
cv.destroyAllWindows()