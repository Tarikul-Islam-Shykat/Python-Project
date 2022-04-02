import  cv2
from tracker import  *

tracker = EuclideanDistTracker()
cap = cv2.VideoCapture("res/highway.mp4")
#object detectation
object_detector = cv2.createBackgroundSubtractorMOG2(history= 100, varThreshold= 40)
'''
this object_detector will extract the moving object from a stable camera.
history > 
varThreshold > the lower it gets the more value we get. 
'''
while True:
    ret, frame = cap.read()
    # extract region from interest
    height, width,_ = frame.shape

    roi = frame[340: 720,500:800] # height and width to crop and focus on that part

    # 1. object detection
    mask = object_detector.apply(roi)# Object Detectation
    _ , mask = cv2.threshold(mask, 254, 255, cv2.THRESH_BINARY) # it will remove all the shadow of the vehicle
    '''
    goal of the mask is everything we dont want is black and 
    the thing we want is white 
    '''
    contours, hierchy =cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    detection = []
    for cnt in contours:
        area = cv2.contourArea(cnt) # calculate area and remvoe small element
        if area> 100:
            x,y,w,h = cv2.boundingRect(cnt)
            cv2.rectangle(roi, (x,y), (x+w, y+h), (0,250,0), 3) # creates rectange for the vehicle
            detection.append([x,y,w,h])

    # object tracking
    boxes_ids = tracker.update(detection)
    for boxes_id in boxes_ids:
        x,y,w,h,id = boxes_id
        cv2.putText(roi, str(id), (x,y-15), cv2.FONT_HERSHEY_PLAIN, 1, (255,0,0) , 2)
        cv2.rectangle(roi, (x, y), (x + w, y + h), (0, 250, 0), 3)

    cv2.imshow("roi", roi)
    cv2.imshow("Frame",frame)
    #cv2.imshow("Mask", mask)
    key = cv2.waitKey(30) # playing video using openCV
    if key == 2:
        break

cap.release()
cv2.destroyAllWindows()
