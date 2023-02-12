import numpy as np
import cv2 as cv

blank = np.zeros((500,500, 3), dtype='uint8')

blank[100:200, 200:400] = 0, 0, 255
cv.imshow ('color', blank)

cv.rectangle(blank, (100,200), (300,blank.shape[1]//2), (255,10,50), thickness=-1)
cv.imshow ('color', blank)

cv.line(blank, (0,0), (blank.shape[0]//2, blank.shape[1]//2), (200,200,250), thickness=3)
cv.circle(blank, (210,211), 200, (0,250,0), thickness=2)
cv.imshow ('color', blank)

cv.putText(blank, 'Putting Text!!!', (150,150),cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), thickness=2)
cv.imshow('color', blank)

cv.waitKey(0)
cv.destroyAllWindows()