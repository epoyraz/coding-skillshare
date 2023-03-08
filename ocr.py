import cv2
import pytesseract

# Load the image
img = cv2.imread('image.jpg')

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply image thresholding
#gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# Apply OCR using pytesseract
text = pytesseract.image_to_string(gray, lang='eng')

# Print the recognized text
print(text)

## blog post
# https://www.kaggle.com/code/dmitryyemelyanov/receipt-ocr-part-2-text-recognition-by-tesseract