import json
import requests
from .card import Card


def jsonize(gameboard):
    # Initalize cards
    card1 = Card('H10', 4, 1)
    card2 = Card('S4', 100, 5)
    jscard1 = json.dumps(card1.__dict__)
    jscard2 = json.dumps(card2.__dict__)

    # Have to .dumps and .loads to avoid problem with "TypeError: Object of type 'Card' is not JSON serializable"
    row1 = [json.loads(jscard1), json.loads(jscard1)]
    row2 = [json.loads(jscard2), json.loads(jscard2)]
    deck = [json.loads(jscard1), json.loads(jscard2), json.loads(jscard1), json.loads(jscard2), json.loads(jscard1), json.loads(jscard2)]

    # Define Data Array (array of arrays.)
    row1 = []
    row2 = []
    row3 = []
    row4 = []
    row5 = []
    row6 = []
    row7 = []
    aces1 = []
    aces2 = []
    aces3 = []
    aces4 = []
    pile = []




    data = [
        row1,
        row2,
        row1,
        row2,
        row1,
        row2,
        row1,
        True,
        False,
        True,
        False,
        deck,
        json.loads(jscard1),
    ]
    print("SENDING OBJECTS \n", data)

    ## Outcommented for merging, waiting for javalin server
    # url = 'http://localhost:8081/Hello'
    # headers = {'Content-Type': "application/json", 'Accept': "application/json"}
    # request = requests.post(url, json=data, headers=headers)

    # print("Hvad der reelt bliver sendt : \n", request.text)

