import  cv2
import  pytesseract

# C:\Users\DOLPHIN\AppData\Local\Programs\Tesseract-OCR > install and save file, change / > //
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\DOLPHIN\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('res/words.JPG')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


# detect only the digit
cong = r'--oem 3 --psm 6 outputbase digits'


hImg, wImg, _ = img.shape
boxes = pytesseract.image_to_boxes(img,config=cong)

for b in boxes.splitlines():
    b = b.split(' ')
    x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
    cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (0, 0, 255),3)  # we get the wrong value if we only provide the (x,y), we have substract the length from the height of the image.
    cv2.putText(img, b[0], (x, hImg - y + 25), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255),2)  # get the string outside of the box

#(x,y-5) >  y-5  will only put the text a litlle bit higher
cv2.imshow("RGB image",img)
cv2.waitKey(0)
