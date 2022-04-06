import  cv2
import  pytesseract

# C:\Users\DOLPHIN\AppData\Local\Programs\Tesseract-OCR > install and save file, change / > //
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\DOLPHIN\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('res/words.JPG')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#print(pytesseract.image_to_boxes(img)) # print text with, x point, y point and w , h diagonal point.

# place the boxes in the image.
hImg, wImg, _ = img.shape
boxes = pytesseract.image_to_boxes(img)

for b in boxes.splitlines():
    #print(b) > H 141 368 200 450 0
    b = b.split()
    x, y,w,h = int(b[1]), int(b[2]),int(b[3]),int(b[4]) # getting the value of x,y and width and height
    cv2.rectangle(img, (x,hImg-y),(w,hImg-h), (0,0,255), 3)
    '''
    we get the wrong value if we only provide the (x,y), we have substract the length from the height of the image.
    '''

cv2.imshow("RGB image",img)
cv2.waitKey(0)
