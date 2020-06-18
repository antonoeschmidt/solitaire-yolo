# from imageproc import chuckify
from flask import Flask
from flask import request
import urllib
app = Flask(__name__)

@app.route('/test', methods=['GET'])
def hello_world():
    # get picture from IMGUR
    url = request.args.get('url')
    print('URL:', url)
    urllib.request.urlretrieve('' + url, 'flask/testFLASK.jpg')

    return 'Hello, World!'


'''
export FLASK_APP=flask/pyServer.py
export FLASK_ENV=development 
flask run
'''