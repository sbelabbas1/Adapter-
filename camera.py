import time
import cv2
#Initiate Port 
camera_port = 1
#Capture Image
camera = cv2.VideoCapture(camera_port)
time.sleep(0.1)  # If you don't wait, the image will be dark
#Save Image
return_value, image = camera.read()
cv2.imwrite("opencv.jpg", image)

# Get user supplied values
imagePath = "C:\Users\steve\Documents\University\2018-2019\Hackathon\Adapter-\opencv.png" #//enter the image path
cascPath = "C:\Users\steve\Documents\University\2018-2019\Hackathon\Face-Detection-OpenCV\data"

# Create the haar cascade
faceCascade = cv2.CascadeClassifier(cascPath)

# Read the image
gray = cv2.imread(imagePath,0) 
#image = cv2.imread(imagePath,0) 
#gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Detect faces in the image
faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    flags=cv2.CASCADE_SCALE_IMAGE, #.cv.CV_HAAR_SCALE_IMAGE
    minSize=(30, 30)
)

# Checks number of humans detected and opens if Monster
if faces < 1:
    print("Machine opens")
else:
    print("Does nothing")
     
    
"""
print("Found {0} faces!".format(len(faces))) 

# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("Faces found", image)
cv2.waitKey(0)
© 2018 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About
Press h to open a hovercard with more details.
del(camera)  # so that others can use the camera as soon as possible

#sudo apt-get install python-opencv
"""