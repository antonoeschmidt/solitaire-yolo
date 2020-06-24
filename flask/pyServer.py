# MODULE_PATH = "/Users/antonoeschmidt/PycharmProjects/solitaire-yolo/yolo/__init__.py"
# MODULE_PATH = "/home/antonio/solitaire-yolo/yolo/__init__.py"
# MODULE_NAME = "yolo"
# import importlib.util
# import sys
# spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
# module = importlib.util.module_from_spec(spec)
# sys.modules[spec.name] = module
# spec.loader.exec_module(module)
from coordinates import rowify

from yolo import imageproc
import sys
#sys.path.append("/Users/antonoeschmidt/PycharmProjects/solitaire-yolo/yolo")
sys.path.append("/home/antonio/solitaire-yolo/yolo")
from yolo.imageproc import chuckify


# from yolo.imageproc import chuckify
# from coordinates import rowify
from flask import Flask
from flask import request
import cv2
import urllib
import cv2
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
    # cards = chuckify('../images/IMG_1488.JPG')
    # for i in cards:
    #    print(i)
    # return 'Success'
    for name in sys.builtin_module_names:
        print(name)

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

# img = cv2.imread('../images/IMG_1488.JPG')
# cards = chuckify(img)
# for i in cards:
#     print(i.suitNumber)
# cv2.imshow('Final', img)
# cv2.waitKey(0)
# cv2.destroyWindow('Finall')
rowify(r'C:\Users\swold\PycharmProjects\solitaire-yolo\images\solitaire-test04.jpg')

# rowify('../images/IMG_1488.JPG')
for d in sys.path:
    print(d)

