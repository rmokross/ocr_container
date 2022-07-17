import cv2
import numpy as np

def imgBuilder(str_img : bytes):
    img_as_np = np.frombuffer(str_img, dtype=np.uint8)
    image = cv2.imdecode(img_as_np, 1)
    return(image)

# create grayscaled image from string image input
def gsImage(img):
    # decode image
    gs_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    return(gs_image)


# create binarized image from grayscaled image 
def binarImage(img : np.ndarray):
    gray_image = gsImage(img)
    thresh, im_bw = cv2.threshold(gray_image, 210, 230, cv2.THRESH_BINARY)
    return(im_bw)
    """
    use img_binarize(string_image) to return binarized image as array
    """

# remove noise 
def rmvNoise(image):
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.dilate(image, kernel, iterations=1)
    kernel = np.ones((1, 1), np.uint8)
    image = cv2.erode(image, kernel, iterations=1)
    image = cv2.morphologyEx(image, cv2.MORPH_CLOSE, kernel)
    image = cv2.medianBlur(image, 3)
    return(image)
