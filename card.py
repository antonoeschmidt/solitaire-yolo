class Card(object):
    def __init__(self, suitNnumber, x, y, picNumber):
        self.suitNumber = suitNnumber
        self.x = x
        self.y = y
        self.picNumber = picNumber
        self.suit = suitNnumber[0:1]

        h = suitNnumber[1:len(suitNnumber)]
        if h == 'h':
            h = 1
        if h == 'd':
            h == 2
        if h == 'c':
            h == 3
        if h == 's':
            h == 4

        self.value = h