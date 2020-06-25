from .yolo.imageproc import chuckify
import math

def getCoordinates(img):
    buffer = 72

    x_size = img.shape[1]
    y_size = img.shape[0]
    cols = round(x_size / 700)
    rows = round(y_size / 700)
    box_x = round(x_size / cols)
    box_y = round(y_size / rows)
    variable_top_row = rows - 1

    final_cards = []

    cards = chuckify(img)

    for current in cards:
        global_x = current.x
        global_y = current.y
        if current.picNumber > rows:
            global_x -= buffer
            global_x += math.floor(((current.picNumber - 1) / rows)) * box_x
        if current.picNumber % rows != variable_top_row:
            global_y -= buffer
            global_y += ((current.picNumber - 1) % rows) * box_y
        current.x = global_x
        current.y = global_y
        final_cards.append(current)

    return final_cards


def rowify(image):
    list2d = []
    list2dAverages = []
    final_rows = []

    rowList = []
    acesList = []
    pile = []

    rowNumber = 0
    xLeeway = 400
    yLeeway = 400

    cards = getCoordinates(image)
    cards_read = cards.copy()

    while len(cards) != 0:
        currentSet = []
        finalSet = []

        cards.sort(key=lambda card: card.x, reverse=False)

        currentSet.append(cards[0])
        currentCard = cards[0]
        currX = currentSet[0].x
        currY = currentSet[0].y

        for i in cards:
            if i.x != currentCard.x:
                if xLeeway >= (i.x - currX) >= -xLeeway:
                    currentSet.append(i)

        currentSet.sort(key=lambda card: card.y, reverse=False)

        finalSet.append(currentSet[0])
        cards.remove(currentSet[0])
        currentSet.remove(currentSet[0])

        for i in currentSet:
            if 0 < i.y - finalSet[len(finalSet) - 1].y <= 300 \
                    and i.value == (finalSet[len(finalSet) - 1].value - 1) \
                    and i.color + finalSet[len(finalSet) - 1].color == 0:
                finalSet.append(i)
                cards.remove(i)
                # currentSet.remove(i)
        list2d.append(finalSet)

    for i in range(len(list2d)):
        averageX = 0
        averageY = 0
        for j in list2d[i]:
            averageX += j.x
            averageY += j.y

        averageX /= len(list2d[i])
        averageY /= len(list2d[i])
        list2dAverages.append([i, averageX, averageY])

    list2dAverages.sort(key=lambda list2dAverages: list2dAverages[1], reverse=False)

    metaRowList = []

    for i in list2dAverages:
        if i[2] < 350:
            if i[1] < 650:
                pile.append(list2d[i[0]])
            else:
                acesList.append(list2d[i[0]])
        else:
            rowList.append(list2d[i[0]])
            metaRowList.append(i)

    missingRows = 7 - len(rowList)

    if missingRows > 0:
        hopList = []
        start = 0
        hop = 0
        for i in range(len(rowList)):
            hop = metaRowList[i][1] - start
            if i == 0:
                hop += 150
            hopList.append(hop)
            start = metaRowList[i][1]
        maxHops = []

        for i in range(missingRows):
            indexMaxHop = 0
            currentMax = 0
            for j in range(len(hopList)):
                if hopList[j] > currentMax:
                    currentMax = hopList[j]
                    indexMaxHop = j
            if currentMax >= 300:
                maxHops.append([indexMaxHop, currentMax])
                hopList[indexMaxHop] = -1

        list2dAverages.sort(key=lambda list2dAverages: list2dAverages[1], reverse=False)

        maxHops.sort(key=lambda maxHops: maxHops[1], reverse=True)
        emptyList = []
        for i in range(missingRows):

            rowList.insert(maxHops[0][0], emptyList)
            maxHops[0][1] -= 300
            for j in maxHops:
                if j[0] > maxHops[0][0]:
                    j[0] += 1
            maxHops.sort(key=lambda maxHops: maxHops[1], reverse=True)

    # order acesList (and add empty lists if necessary)
    emptyAces = []


    if len(acesList) != 0:
        missingLists = 4 - len(acesList)
        for i in range(missingLists):
            acesList.append(emptyAces)

        xx = 0
        while xx < 4:
            increment = True
            if len(acesList[xx]) != 0:
                tempSwitch = []
                if acesList[xx][0].suit != xx:
                    tempSwitch = acesList[acesList[xx][0].suit]
                    acesList[acesList[xx][0].suit] = acesList[xx]
                    acesList[xx] = tempSwitch
                    xx = 0
                    increment = False
            if increment:
                xx += 1
    else:
        for i in range(4):
            acesList.append(emptyAces)

    if len(pile) == 0:
        emptyPile = []
        pile.append(emptyPile)

    gameBoard = []
    gameBoard.append(rowList)
    gameBoard.append(acesList)
    gameBoard.append(pile)
    return gameBoard