import json
import requests
# from card import Card


def jsonize(gameboard):
    data = []

    # Define Data Array (array of arrays.)
    dataLocation = 0
    for i in range(3):
        for j in range(len(gameboard[i])):
            list = []
            for k in range(len(gameboard[i][j])):
                current = json.dumps(gameboard[i][j][k].__dict__)
                list.insert(0, json.loads(current))
            data.insert(dataLocation, list)
            dataLocation += 1

    print("SENDING OBJECTS \n", json=data)

    # url = 'http://localhost:8081/Hello'
    # headers = {'Content-Type': "application/json", 'Accept': "application/json"}
    # request = requests.post(url, json=data, headers=headers)
    #
    # print("Hvad der reelt bliver sendt : \n", request.text)