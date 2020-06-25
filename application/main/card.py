class Card(object):

    def __init__(self, suitNnumber, x, y, picNumber):
        self.suitNumber = suitNnumber
        self.x = x
        self.y = y
        self.picNumber = picNumber

        suitLetter = suitNnumber[0:1]
        valueString = suitNnumber[1:len(suitNnumber)]
        h = 0
        color = 0
        if suitLetter == 'h':
            h = 1
            color = 1
        if suitLetter == 'd':
            h = 0
            color = 1
        if suitLetter == 'c':
            h = 3
            color = -1
        if suitLetter == 's':
            h = 2
            color = -1

        self.suit = h
        self.value = int(valueString)
        self.color = color