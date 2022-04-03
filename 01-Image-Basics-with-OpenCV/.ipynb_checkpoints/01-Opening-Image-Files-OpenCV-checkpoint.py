import cv2

img = cv2.imread('../DATA/00-puppy.jpg',cv2.IMREAD_GRAYSCALE)
# Show the image with OpenCV
cv2.imshow('window_name',img)
# Wait for something on keyboard to be pressed to close window.
cv2.waitKey()