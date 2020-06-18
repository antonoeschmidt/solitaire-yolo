from imageproc import chuckify
import cv2
import math
from card import Card

def run():
    img = cv2.imread('images/test1.png')

    buffer = 100

    x_size = img.shape[1]
    y_size = img.shape[0]
    cols = round(x_size/700)
    rows = round(y_size/700)

    final_cards = []

    cards = chuckify(img)

    for current in cards:
        global_x = current.x
        global_y = current.y
        if current.picNumber > rows:
            global_x -= buffer
            global_x += math.floor(((current.picNumber-1) / rows)) * x_size
        if current.picNumber % cols != 1:
            global_y -= buffer
            global_y += ((current.picNumber % cols) -1) * y_size
        current.x = global_x
        current.y = global_y
        final_cards.append(current)
    return final_cards


