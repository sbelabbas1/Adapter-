import time
import cv2


def convertToRGB(img): 
    return cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

def detect_faces(f_cascade, colored_img, scaleFactor = 1.1):
 #just making a copy of image passed, so that passed image is not changed 
 img_copy = colored_img.copy()          
 
 #convert the test image to gray image as opencv face detector expects gray images
 gray = cv2.cvtColor(img_copy, cv2.COLOR_BGR2GRAY)          
 
 #let's detect multiscale (some images may be closer to camera than others) images
 faces = f_cascade.detectMultiScale(gray, scaleFactor=scaleFactor, minNeighbors=5);          
 
 #go over list of faces and draw them as rectangles on original colored img
 for (x, y, w, h) in faces:
      cv2.rectangle(img_copy, (x, y), (x+w, y+h), (0, 255, 0), 2)              
 
 return img_copy

#Initiate Port 
camera_port = 1
#Capture Image
camera = cv2.VideoCapture(camera_port)
time.sleep(0.1)  # If you don't wait, the image will be dark
#Save Image
return_value, image = camera.read()

haar_face_cascade = cv2.CascadeClassifier('C:\Users\steve\Documents\University\2018-2019\Hackathon\Adapter-\data')

cv2.imwrite("opencv.png", image)

test2 = cv2.imread('opencv.png')  
 
#call our function to detect faces 
faces_detected_img = detect_faces(haar_face_cascade, test2)  
 
#convert image to RGB and show image 
plt.imshow(convertToRGB(faces_detected_img))
