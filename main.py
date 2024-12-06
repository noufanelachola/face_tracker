import cv2 as cv

capture = cv.VideoCapture(0)
while True:
    isTrue, frame = capture.read()
    cv.imshow("Video Capture",frame)
    
    if not isTrue:
        print("Failed to read frame.")
        break

    if cv.waitKey(20) & 0xFF == ord('d') :
        break

capture.release()
cv.destroyAllWindows()


