import cv2
import os

path = os.getcwd()

print(path)
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
img = cv2.imread('news.jpg')
print(img)
x = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(x,
scaleFactor=1.1,
minNeighbors=5)

for x,y,w,h in faces:
    x=cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
print(type(faces))
print(faces)
resized=cv2.resize(img,(int(img.shape[1]/3),int(img.shape[0]/3)))
cv2.imshow("Gray",resized)

cv2.imshow("Gray", x)
cv2.waitKey(0)
cv2.destroyAllWindows()
