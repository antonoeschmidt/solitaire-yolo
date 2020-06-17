import cv2
from yolo.yolo3 import detect

def chuckify(img, cols, rows):
    # cv2.imread(img)

    sizeX = img.shape[1]
    print('sizeX: ', sizeX)
    sizeY = img.shape[0]
    print('sizeY: ', sizeY)

    buffer = 50

    for i in range(0, sizeX, int(sizeX/cols)):
        for j in range(0, sizeY-1, int(sizeY/rows)):
            cv2.rectangle(img, (i, j), (i + (int(sizeX/cols)) + buffer, j + (int(sizeY/rows)) + buffer), (255, 255, 0), 2)
            # cv2.imshow("123", img)
            # cv2.waiqtKey(0)
            # cv2.destroyWindow('123')
            #test = img[(i, j), (i + (int(sizeX/cols)) + buffer, j + (int(sizeY/rows)) + buffer)].copy()
            #test = img[0:600, 400:800]
            #test = img[i:i + (int(sizeX/cols)) + buffer, j + (int(sizeY/rows))]
            test = img[j : j + (int(sizeY/rows)) + buffer, i:i + (int(sizeX/cols)) + buffer]
            print(test.shape)
            cv2.imshow('testcrop', test)
            cv2.waitKey(0)
            cv2.destroyWindow('testcrop')
            detect(test)

    #test = img[0:100, 0:800]
    #cv2.imshow('testcrop', test)
    #cv2.imshow("123", img)
    #cv2.waitKey(0)
    #cv2.destroyWindow('testcrop')
    #cv2.destroyWindow('123')


img = cv2.imread('images/IMG_1485.jpg')
chuckify(img, 3, 3)

# img = cv2.imread('images/fd3.png')
# detect(img)
