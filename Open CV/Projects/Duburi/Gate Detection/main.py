import cv2
import  numpy as np

def nothing():
    pass

cap = cv2.VideoCapture(0)

# create a track bar to get the value
cv2.namedWindow("Track")
cv2.createTrackbar("L-H", "Track", 0, 180, nothing)
cv2.createTrackbar("L-S", "Track", 59, 255, nothing)
cv2.createTrackbar("L-V", "Track", 0, 255, nothing)
cv2.createTrackbar("U-H", "Track", 12, 255, nothing)
cv2.createTrackbar("U-S", "Track", 248, 255, nothing)
cv2.createTrackbar("U-V", "Track",  255, 255, nothing)


while True:
    _, frame = cap.read()

    blurred_frame = cv2.GaussianBlur(frame, (5,5), 0)
    hsv_frame = cv2.cvtColor(blurred_frame, cv2.COLOR_BGR2HSV)

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


    # conturs detection
    contours, hierarchy = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area > 100:
            x, y, w, h = cv2.boundingRect(cnt)
            #print(f'x = {x}, y = {y}, w = {w}, h = {h} ')
            if x > 100  and y > 100 and w > 100 and w < 350 and  h > 55:
                img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 250, 0), 3)
                cv2.putText(img, 'Gate', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36, 255, 12), 2)
    cv2.imshow("Frame", frame)
    cv2.imshow("Red", mask)
    #cv2.imshow("kd", kernal)
    key = cv2.waitKey(1)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()
