import numpy as np
import urllib
import cv2
from imgurpython import ImgurClient

client_id = 'd690f59a4a3e69e'
client_secret = '17ef771a862e57aa8c391b158dd887d6934f5f50'
access_token = 'b33d6c7f46b12a18210f1462f044f79d955984cd'
refresh_token = ''

urls = [
    "https://pyimagesearch.com/wp-content/uploads/2015/01/opencv_logo.png",
    "https://pyimagesearch.com/wp-content/uploads/2015/01/google_logo.png",
    "https://pyimagesearch.com/wp-content/uploads/2014/12/adrian_face_detection_sidebar.png",
]

client = ImgurClient(client_id, client_secret)

item = client.get_image('aZayn96')
print(item.title)
print(item.description) # printer description for photo

# få username og kald items.


# image = cv2.imread('https://imgur.com/aZayn96')
# cv2.namedWindow('YOLO', cv2.WINDOW_NORMAL)
# cv2.imshow('HEJ', image)

# METHOD #1: OpenCV, NumPy, and urllib
# def url_to_image(url):
#     # download the image, convert it to a NumPy array, and then read
#     # it into OpenCV format
#     resp = urllib.urlopen(url)
#     image = np.asarray(bytearray(resp.read()), dtype="uint8")
#     image = cv2.imdecode(image, cv2.IMREAD_COLOR)
#     # return the image
#     return image
#
#
# for url in urls:
#     # download the image URL and display it
#     print("downloading %s" % (url))
#     image = url_to_image(url)
#     cv2.imshow("Image", image)
#     cv2.waitKey(0)

# client = ImgurClient(client_id, client_secret, access_token, refresh_token)

# image = client.get_image('aZayn96')
# image.
# client.delete_image(image)

# image_BGR = cv2.imread('images/full_deck.png')
