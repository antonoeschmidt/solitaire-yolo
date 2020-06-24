from main.yolo.imageproc import chuckify
import cv2

img = cv2.imread('../images/IMG_1488.JPG')
chuckify(img)
print('loaded')