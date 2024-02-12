import cv2

#from google.colab import files

#from IPython display import Image, display

uploaded files.upload()

image_path = list(uploaded.keys())[0] 
Image = cv2.imread(image_path)

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#Load the pre-trained Haar Cascade Classifier for face detection face 
cv2.CascadeClassifier(cv2.data.haarcascadeshaarcascade "frontalface_default.xml")

#Perform face detectionfaces 
face_cascade.detectMultiScale(gray image, scaleFactor-1.3, minNeighbors=5)

#Draw rectangles around the detected faces

for (x, y, w, h) in faces: 
    cv2.rectangle(image, (x, y), (x+w, y+h). (255, 0, 0), 2)

#Display the image with detected faces 
    cv2.imwrite('result.jpg', image) 
    cv2.display(Image(filename=result.jpg"))