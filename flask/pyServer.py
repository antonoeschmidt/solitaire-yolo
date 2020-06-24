from yolo.imageproc import chuckify
from coordinates import rowify
from flask import Flask
from flask import request
import cv2
import urllib
app = Flask(__name__)



@app.route('/test', methods=['GET'])
def getPicture():
    # get picture from IMGUR
    url = request.args.get('url')
    print('URL:', url)
    resp = urllib.request.urlretrieve('' + url, 'flask/testFLASK.jpg')
    print(resp.code)
    return 'Success'

@app.route('/mark', methods=['GET'])
def mark():
    cards = chuckify('../images/IMG_1488.JPG')
    for i in cards:
        print(i)
    return 'Success'

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

export FLASK_APP=flask/pyServer.py
export FLASK_ENV=development 
flask run
flask run --host=0.0.0.0 --port=80

'''
# url = 'https://i.imgur.com/96xIyVb.jpg'
# h, resp = urllib.request.urlretrieve(url, 'testFLASK.jpg')
# print(resp)

img = cv2.imread('../images/IMG_1488.JPG')
cards = chuckify(img)
# for i in cards:
#     print(i.suitNumber)
# cv2.imshow('Final', img)
# cv2.waitKey(0)
# cv2.destroyWindow('Finall')
# rowify('../images/IMG_1488.JPG')