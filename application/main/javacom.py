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

    print("SENDING OBJECTS \n", data)

    print("Actual JSON")
    my_json_string = json.dumps(data)
    print(my_json_string)

    # url = 'http://35.246.214.109:3333/Hello'
    # headers = {'Content-Type': "application/json", 'Accept': "application/json"}
    # request = requests.post(url, json=data, headers=headers)
    #
    # print("Hvad der reelt bliver sendt : \n", request.text)

    return my_json_string