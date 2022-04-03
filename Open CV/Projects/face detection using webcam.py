import cv2

cap = cv2.VideoCapture(0)
casscase_classifier = cv2.CascadeClassifier('res/haarcascade_frontalface_default.xml')



while True:
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, 0)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    detectction = casscase_classifier.detectMultiScale(gray, 1.3, 5)

    if(len(detectction)>0):
        (x,y,w,h) = detectction[0]
        frame = cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 2)

    cv2.imshow('frame', frame)
    if   cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
