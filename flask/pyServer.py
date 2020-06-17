from imageproc import chuckify
from flask import Flask
app = Flask(__name__)

@app.route('/test', methods=['GET'])
def hello_world():
    # get picture from IMGUR

    #chuckify(image)
    cards = []

    return 'Hello, World!'
