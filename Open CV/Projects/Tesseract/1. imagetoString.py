import  cv2
import  pytesseract

# C:\Users\DOLPHIN\AppData\Local\Programs\Tesseract-OCR > install and save file, change / > //
pytesseract.pytesseract.tesseract_cmd = 'C:\\Users\\DOLPHIN\\AppData\\Local\\Programs\\Tesseract-OCR\\tesseract.exe'


#py tessarace only accept rgb value and open cv in in bgr, so we have to convert it.

img = cv2.imread('res/words.JPG')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

print(pytesseract.image_to_string(img)) # prints all the word in image. 

cv2.imshow("RGB image ",img)
cv2.waitKey(0)

