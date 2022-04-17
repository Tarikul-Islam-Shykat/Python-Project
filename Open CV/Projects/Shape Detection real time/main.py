import cv2
import  numpy as np

def nothing():
    pass

cap = cv2.VideoCapture(0)

# create a track bar to get the value
cv2.namedWindow("Track")
cv2.createTrackbar("L-H", "Track", 0, 180, nothing)
cv2.createTrackbar("L-S", "Track", 68, 255, nothing)
cv2.createTrackbar("L-V", "Track", 154, 255, nothing)
cv2.createTrackbar("U-H", "Track", 180, 180, nothing)
cv2.createTrackbar("U-S", "Track", 255, 255, nothing)
cv2.createTrackbar("U-V", "Track",  243, 255, nothing)

while True:
    _, frame = cap.read()

    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    l_h = cv2.getTrackbarPos("L-H","Track" )
    l_s = cv2.getTrackbarPos("L-S", "Track")
    l_v = cv2.getTrackbarPos("L-V", "Track")

    u_h = cv2.getTrackbarPos("U-H", "Track")
    u_s = cv2.getTrackbarPos("U-S", "Track")
    u_v = cv2.getTrackbarPos("U-V", "Track")

    # mask for red color
    low_red = np.array([l_h, l_s, l_v]) # use track bar to get the red portion white and get the perfect value
    high_red = np.array([u_h, u_s, u_v])
    mask = cv2.inRange(hsv_frame, low_red, high_red)  # only define the red color

    kernal = np.ones((5,5), np.uint8) # for black sqaure
    mask = cv2.erode(mask, kernal)


    # conturs detection
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        approx = cv2.approxPolyDP(cnt, 0.01 * cv2.arcLength(cnt, True), True )
        if area > 400:
            cv2.drawContours(frame, [approx], 0, (0, 0, 0), 5)
            if len(approx) == 4 :
                cv2.putText(frame, "Rectangle", (10,10), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0))


    cv2.imshow("Frame", frame)
    cv2.imshow("Red", mask)
    cv2.imshow("kd", kernal)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()

'''
1st we detected the object with color.

2nd we detected the contours.

3rd step detect the shape of contours.
'''
