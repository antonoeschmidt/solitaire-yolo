"""
@author: Anton Østergaard Schmidt, s163053

"""

from main import app

import pathlib
print(pathlib.Path().absolute())

from .yolo import imageproc

from .coordinates import rowify
from flask import Flask, Blueprint
from flask import request
import urllib
import cv2
import time as t
from .javacom import jsonize

bp = Blueprint("auth", __name__, url_prefix="/auth")

@app.route('/', methods=['GET'])
def home():
    return 'Success'

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
    start = t.time()
    img = cv2.imread('/home/antonio/solitaire-yolo/application/main/images/IMG_1488.JPG')
    cards = imageproc.chuckify(img)
    end = t.time()
    time = end - start
    for i in cards:
        print(i.suitNumber)
    return 'Processing took ' + str(time) + ' seconds.'

@app.route('/testpicture', methods=['GET'])
def testingpicture():
    # get picture from IMGUR
    url = request.args.get('url')
    urllib.request.urlretrieve(url, '/home/antonio/solitaire-yolo/application/main/images/newest.jpg')
    img = cv2.imread('/home/antonio/solitaire-yolo/application/main/images/newest.jpg')
    start = t.time()
    gameboard = rowify(img)
    jsonstring = jsonize(gameboard)
    end = t.time()
    time = end - start

    print('URL:', url)
    # return 'Success. Received url was: ' + url + '. Processing took ' + str(time)
    return jsonstring

@app.route('/quit')
def quit():
    func = request.environ.get('werkzeug.server.shutdown')
    func()
    return "Quitting..."

'''
** Commands needed to run FLASK server **

export FLASK_APP=pyServer.py
export FLASK_ENV=development 
flask_server run
flask_server run --host=0.0.0.0 --port=80
'''
