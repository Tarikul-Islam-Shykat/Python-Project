import  cv2
import  pytesseract

# C:\Users\DOLPHIN\AppData\Local\Programs\Tesseract-OCR > install and save file, change / > //
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\DOLPHIN\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'

img = cv2.imread('res/words.JPG')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

#print(pytesseract.image_to_boxes(img)) # print text with, x point, y point and w , h diagonal point.

# place the boxes in the image.
hImg, wImg, _ = img.shape
boxes = pytesseract.image_to_data(img)

for x,b in enumerate(boxes.splitlines()):
    if x!=0:
        b = b.split()
        print(b)
        if len(b)==12: # only text length more than 12 are only sentecne
            x, y, w, h = int(b[6]), int(b[7]), int(b[8]), int(b[9]) # detect the whole sentence.
            cv2.rectangle(img, (x,y), (x+w, h+y), (0, 0, 255), 3)
            cv2.putText(img, b[11], (x,y-5), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 255),2)  # get the string outside of the box

#(x,y-5) >  y-5  will only put the text a litlle bit higher
cv2.imshow("RGB image",img)
cv2.waitKey(0)
