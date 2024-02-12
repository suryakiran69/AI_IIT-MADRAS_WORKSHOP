#C:\Users\surya\Desktop\download.jpg
import cv2 
image_path='download.jpg'
a=cv2.imread(image_path)
cv2.imshow('Image',a)

gray_image=cv2.cvtColor(a,cv2.COLOR_RGB2GRAY)
cv2.imshow('gray_image',gray_image)


cv2.waitKey(0)
