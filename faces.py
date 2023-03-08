# import required library
import cv2

# read the input image
img = cv2.imread('faces.jpg')

# convert to grayscale of each frames
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# read haacascade to detect faces in input image
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface.xml')

# detects faces in the input image
faces = face_cascade.detectMultiScale(gray, 1.1, 2)
print('Number of detected faces:', len(faces))\

# loop over all the detected faces
for (x,y,w,h) in faces:

   # To draw a rectangle around the detected face  
   cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),10)

# Display an image in a window
cv2.imshow('Face Detection',img)
cv2.waitKey(0)
cv2.destroyAllWindows()