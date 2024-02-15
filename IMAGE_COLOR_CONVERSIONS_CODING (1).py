

# import cv2
# from google.colab.patches import cv2_imshow
import cv2
import numpy as np

#read and diplay image
img=cv2.imread("img.png")
cv2.imshow("window",img)
cv2.waitKey(0)

#WRITE AN IMAGE
# Save the original image to a file
original_output_path = "original_image.png"
cv2.imwrite(original_output_path, img)
print(f"Original image saved to: {original_output_path}")

# Read the saved image
saved_image = cv2.imread(original_output_path)

# Display the saved image
cv2.imshow("window",saved_image)

# Save the saved image to a new file
new_output_path = "saved_image.png"
cv2.imwrite(new_output_path, saved_image)
print(f"Saved image saved to: {new_output_path}")

#ACCESSING ROWS AND COLUMNS
rows, columns, channels = img.shape
print(f"Image Shape: Rows={rows}, Columns={columns}, Channels={channels}")

import random
for i in range (100):
    for j in range(img.shape[1]):
        img[i][j] = [random.randint(0,255),random.randint(0,255),random.randint(0,255)]
cv2.imshow('part image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


#Cut and paste the image
image=cv2.imread("rose.png")
tag = image[300:400,300:400]
image[50:150,50:150] = tag
cv2.imshow('partimage1',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#######COLOR CONVERSION
##Convert BGR and RGB to HSV and GRAY

# Display the original BGR image
color_image=cv2.imread('img.png')
cv2.imshow('Original Image',color_image)

# Convert BGR to HSV
bgr_hsv = cv2.cvtColor(color_image,cv2.COLOR_BGR2HSV)
cv2.imshow('BGR2HSV',bgr_hsv)

# Convert RGB to HSV
rgb_hsv = cv2.cvtColor(color_image,cv2.COLOR_RGB2HSV)
cv2.imshow('RGB2HSV',rgb_hsv)

# Convert BGR to Grayscale
bgr_gray = cv2.cvtColor(color_image,cv2.COLOR_BGR2GRAY)
cv2.imshow('BGR2GRAY',bgr_gray)

# Convert RGB to Grayscale
rgb_gray = cv2.cvtColor(color_image,cv2.COLOR_RGB2GRAY)
cv2.imshow('RGB2GRAY',rgb_gray)

cv2.waitKey(0)
cv2.destoryAllWindow()

##Convert HSV to RGB and BGR

import cv2
hsv=cv2.imread('hsvimg.png')
cv2.imshow('Original HSV image',hsv)
rgb_img=cv2.cvtColor(hsv,cv2.COLOR_HSV2RGB)
cv2.imshow('HSV to RGB',rgb_img)
bgr_img=cv2.cvtColor(hsv,cv2.COLOR_HSV2BGR)
cv2.imshow('HSV to BGR',bgr_img)

cv2.waitKey(0)
cv2.destoryAllWindow()


##Convert RGB and BGR to YCrCb


img=cv2.imread("img.png")
YCrCb_image = cv2.cvtColor(img, cv2.COLOR_RGB2YCrCb)
cv2.imshow('RGB to YCrCb',YCrCb_image)
YCrCb_image1 = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
cv2.imshow('BGR to YCrCb',YCrCb_image1)


cv2.waitKey(0)
cv2.destoryAllWindow()

#Split and Merge RGB Image


blue = img[:,:,0]
green = img[:,:,1]
red = img[:,:,2]

cv2.merge((blue,green,red))


##Split and merge HSV Image


h, s, v = cv2.split(hsv)

cv2.merge((h,s,v))




