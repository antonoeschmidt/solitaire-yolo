from imageproc import chuckify
import cv2
import math
from card import Card

img = cv2.imread('images/test1.png')
d = 3
buffer = 100
x_size = 700
y_size = 700
final_cards = []

cards = chuckify(img, 3, 3)

for current in cards:
    global_x = current.x
    global_y = current.y
    if current.picNumber > d:
        global_x -= buffer
        global_x += math.floor(((current.picNumber-1) / d)) * x_size
    if current.picNumber % d != 1:
        global_y -= buffer
        global_y += ((current.picNumber % d) -1) * y_size
    current.x = global_x
    current.y = global_y

for i in cards:
    print('n ', i.picNumber)
    print('x ', i.x)
    print('y ', i.y)
    print()


