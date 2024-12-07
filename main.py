import cv2 as cv

haar_cascade = cv.CascadeClassifier("haarcascade_frontalface_default.xml")

capture = cv.VideoCapture(0)

while True: 
    isTrue, frame = capture.read()
    
    if not isTrue:
        print("Failed to read frame.")
        break
    else:

        gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        cv.imshow("Gray",gray)

        faces = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5)

        for (x,y,w,h) in faces:
            cv.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),thickness=2)

        cv.imshow("Video Capture",frame)
        
        if cv.waitKey(20) & 0xFF == ord('d') :
            break


capture.release()
cv.destroyAllWindows()


