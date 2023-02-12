import cv2 as cv

capture = cv.VideoCapture(0)

while True:
    isTrue, frame = capture.read()
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    canny = cv.Canny(frame, 100, 100)
    cv.imshow('canny', canny)
    cv.imshow('gray', gray)

    haar = cv.CascadeClassifier('haar_face.xml')

    face = haar.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    for (x,y,w,h) in face:
        cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

    cv.imshow('live',frame)

    if cv.waitKey(20) & 0xFF == ord('c'):
        break

capture.release()
cv.destroyAllWindows()