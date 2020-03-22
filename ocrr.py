
# coding: utf-8

# In[3]:


from PIL import Image
import pytesseract
import argparse
import cv2
import os
 
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image to be OCR'd")
ap.add_argument("-p", "--preprocess", type=str, default="thresh", help="type of preprocessing to be done")
args = vars(ap.parse_args())

# load the example image and convert it to grayscale
image = cv2.imread(args["image"])
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 
# check to see if we should apply thresholding to preprocess the
# image
if args["preprocess"] == "thresh":
     #cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
     gray = cv2.medianBlur(gray, 1)
     gray = cv2.adaptiveThreshold(gray,350,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,15)
#gray = cv2.GaussianBlur(gray,(5,5),0)
     #gray,a = cv2.threshold(gray,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
     #gray = cv2.threshold(gray,0,255,cv2.THRESH_BINARY)
     #gray = cv2.medianBlur(gray, 1)
     #gray = cv2.bilateralFilter(gray,9,75,75)
     
#gray = cv2.adaptiveThreshold(gray,350,cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,11,5)
#gray = cv2.threshold(gray, 0, 256, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
#cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\cv2.THRESH_BINARY,11,2)

#cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
 
# make a check to see if median blurring should be done to remove
# noise
#if args["preprocess"] == "blur":
 #   gray = cv2.medianBlur(gray, 2)
 
# write the grayscale image to disk as a temporary file so we can
# apply OCR to it
filename = "{}.png".format(os.getpid())
cv2.imwrite(filename, gray)

# load the image as a PIL/Pillow image, apply OCR, and then delete
# the temporary file
text = pytesseract.image_to_data(Image.open(filename), lang = "tur")
os.remove(filename)
print(text)
 
# show the output images
#cv2.imshow("Image", image)
cv2.imshow("Output", gray)
cv2.waitKey(0)
