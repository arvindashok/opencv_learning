import cv2 as cv

img = cv.imread('sidemen.jpeg')
# cv.imshow('jj',img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

canny = cv.Canny(img, 100, 100)
# cv.imshow('canny',canny)

haar_cascade = cv.CascadeClassifier('haar_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
print (len(faces_rect))

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 1)

cv.imshow('jj',img)

cv.waitKey(0)
cv.destroyAllWindows()