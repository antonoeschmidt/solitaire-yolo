from application import app
import sys
# sys.path.append("/Users/antonoeschmidt/PycharmProjects/solitaire-yolo/yolo")
# sys.path.append("/home/antonio/solitaire-yolo/yolo")

import pathlib
print(pathlib.Path().absolute())

from yolo.imageproc import chuckify
# from main.yolo.imageproc import chuckify

# from coordinates import rowify
from flask import Flask
from flask import request
import urllib
app = Flask(__name__)


@app.route('/test', methods=['GET'])
def getPicture():
    # get picture from IMGUR
    url = request.args.get('url')
    print('URL:', url)
    resp = urllib.request.urlretrieve('' + url, 'flask_server/testFLASK.jpg')
    print(resp.code)
    return 'Success'

@app.route('/mark', methods=['GET'])
def mark():
    # cards = chuckify('../images/IMG_1488.JPG')
    # for i in cards:
    #    print(i)
    # return 'Success'
    for name in sys.builtin_module_names:
        print(name)
    return 'Mark'

@app.route('/testpicture', methods=['GET'])
def testingpicture():
    # get picture from IMGUR
    url = request.args.get('url')
    print('URL:', url)
    return 'Success. Received url was: ' + url

@app.route('/quit')
def quit():
    func = request.environ.get('werkzeug.server.shutdown')
    func()
    return "Quitting..."
'''
** Commands needed to run FLASK server **

export FLASK_APP=flask_server/pyServer.py
export FLASK_ENV=development 
flask_server run
flask_server run --host=0.0.0.0 --port=80

'''
# url = 'https://i.imgur.com/96xIyVb.jpg'
# h, resp = urllib.request.urlretrieve(url, 'testFLASK.jpg')
# print(resp)

# img = cv2.imread('../images/IMG_1488.JPG')
# cards = chuckify(img)
# for i in cards:
#     print(i.suitNumber)
# cv2.imshow('Final', img)
# cv2.waitKey(0)
# cv2.destroyWindow('Finall')
# rowify('../images/IMG_1488.JPG')
# for d in sys.path:
  #  print(d)
import cv2
img = cv2.imread('images/IMG_1488.JPG')
chuckify(img)