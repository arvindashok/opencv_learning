import cv2 as cv
 
def rescale(frame, scale=0.75):
    height =  int (frame.shape[0] * scale)
    width = int (frame.shape[1] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions)

capture = cv.VideoCapture(0) #capturing video from webcam(0)

def resize(width, height):
    capture.set (3, width)
    capture.set (4, height)

resize(480, 360)

while True:

    isTrue, frame = capture.read() 

    frame_resize1 = rescale(frame) #callling function to scaledown

    conv= cv.cvtColor(frame, cv.COLOR_BGR2GRAY) #changing to grayscale

    cv.imshow('live',frame) 
    # cv.imshow('gray',conv)

    if cv.waitKey(20) & 0xFF == ord('c'):
        break

    elif cv.waitKey(20) & 0xFF == ord('g'):
        cv.imshow('gray',conv)

capture.release()
cv.destroyAllWindows()