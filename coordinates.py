from yolo.imageproc import chuckify
import cv2
import math



def getCoordinates():
    img = cv2.imread('images/test1.png')

    buffer = 100

    x_size = img.shape[1]
    y_size = img.shape[0]
    cols = round(x_size / 700)
    rows = round(y_size / 700)

    final_cards = []

    cards = chuckify(img)

    for current in cards:
        global_x = current.x
        global_y = current.y
        if current.picNumber > rows:
            global_x -= buffer
            global_x += math.floor(((current.picNumber - 1) / rows)) * x_size
        if current.picNumber % cols != 1:
            global_y -= buffer
            global_y += ((current.picNumber % cols) - 1) * y_size
        current.x = global_x
        current.y = global_y
        final_cards.append(current)
    return final_cards


def rowify():

    row1 = []
    row2 = []
    row3 = []
    row4 = []
    row5 = []
    row6 = []
    row7 = []
    a1 = []
    a2 = []
    a3 = []
    a4 = []

    rowNumber = 0
    xLeeway = 100
    yLeeway = 100

    cards = getCoordinates()

    while len(cards) != 0:
        currentSet = []
        finalSet = []

        cards.sort(key=lambda card: card.x, reverse=True)

        currentSet.append(cards[0])
        cards.remove(0)
        currX = currentSet[0].x
        currY = currentSet[0].y


        for i in range(len(cards)):
            if (cards[i].x - currX) >= -xLeeway or (cards[i].x - currX) <= xLeeway:
                currentSet.append(cards[i])
                cards.remove(i)

        currentSet.sort(key=lambda card: card.y, reverse=True)

        finalSet.append(currentSet[0])
        currentSet.remove(0)

        for i in range(len(currentSet)):
            if 0 < currentSet[0].y - finalSet[len(finalSet) - 1] <= 100 \
                    and currentSet[0].suit == finalSet.suit \
                    and currentSet[0].value == finalSet[0].value - 1:
                finalSet.append(currentSet[0])
                currentSet.remove(0)
            else:
                cards.append(currentSet[0])
                currentSet.remove(0)

        if rowNumber == 0:
            row1 = finalSet
        if rowNumber == 1:
            row2 = finalSet
        if rowNumber == 2:
            row3 = finalSet
        if rowNumber == 3:
            row4 = finalSet
        if rowNumber == 4:
            row5 = finalSet
        if rowNumber == 5:
            row6 = finalSet
        if rowNumber == 6:
            row7 = finalSet


        rowNumber = rowNumber + 1




