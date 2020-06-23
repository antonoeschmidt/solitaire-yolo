# from imageproc import chuckify
from flask import Flask
from flask import request
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

@app.route('/test1', methods=['GET'])
def getPicture():
    return 'Success'


'''
** Commands needed to run FLASK server **

export FLASK_APP=flask/pyServer.py
export FLASK_ENV=development 
flask run
flask run --host=0.0.0.0 --port=80

'''
url = 'https://i.imgur.com/96xIyVb.jpg'
h, resp = urllib.request.urlretrieve(url, 'testFLASK.jpg')
print(resp)