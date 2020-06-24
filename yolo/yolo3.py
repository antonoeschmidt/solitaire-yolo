import numpy as np
import cv2
import time
# from card import Card

# MODULE_PATH = "/Users/antonoeschmidt/PycharmProjects/solitaire-yolo/__init__.py"
MODULE_PATH = "/home/antonio/solitaire-yolo/__init__.py"
MODULE_NAME = "card1"
import importlib.util
import sys
spec = importlib.util.spec_from_file_location(MODULE_NAME, MODULE_PATH)
module = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = module
spec.loader.exec_module(module)

from card1 import card
from card import Card

def detect(image_BGR, picNumber, debug='no'):

    # image_BGR = cv2.imread('../images/IMG_1485.jpg')
    if debug == 'yes':
        cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
        cv2.imshow('Original Image', image_BGR)
        cv2.waitKey(0)
        cv2.destroyWindow('Original Image')

    # Showing image shape
    print('Image shape:', image_BGR.shape)  # tuple of (511, 767, 3)
    # Getting spatial dimension of input image
    h, w = image_BGR.shape[:2]  # Slicing from tuple only first two elements

    # Getting blob from input image
    blob = cv2.dnn.blobFromImage(image_BGR, 1 / 255.0, (416, 416),
                                 swapRB=True, crop=False)
    print('Image shape:', image_BGR.shape)  # (511, 767, 3)
    print('Blob shape:', blob.shape)  # (1, 3, 416, 416)
    blob_to_show = blob[0, :, :, :].transpose(1, 2, 0)
    print(blob_to_show.shape)  # (416, 416, 3)

    # Showing Blob Image
    if debug == 'yes':
        cv2.namedWindow('Blob Image', cv2.WINDOW_NORMAL)
        cv2.imshow('Blob Image', cv2.cvtColor(blob_to_show, cv2.COLOR_RGB2BGR))
        cv2.waitKey(0)
        cv2.destroyWindow('Blob Image')

    # Loading class labels from file
    with open('../config/classes.names') as f:
        labels = [line.strip() for line in f]

    print('List with labels names:')
    print(labels)

    # Loading trained YOLO v3 Objects Detector
    network = cv2.dnn.readNetFromDarknet('../config/full_set.cfg',
                                         '../config/full_set_00001_4000.weights')

    # Getting list with names of all layers from YOLO v3 network
    layers_names_all = network.getLayerNames()

    # Getting only output layers' names that we need from YOLO v3 algorithm
    # with function that returns indexes of layers with unconnected outputs
    layers_names_output = \
        [layers_names_all[i[0] - 1] for i in network.getUnconnectedOutLayers()]

    # Setting minimum probability to eliminate weak predictions
    probability_minimum = 0.5

    # Setting threshold for filtering weak bounding boxes with non-maximum suppression
    threshold = 0.3

    # Generating colours for representing every detected object
    colours = np.random.randint(0, 255, size=(len(labels), 3), dtype='uint8')

    network.setInput(blob)  # setting blob as input to the network
    start = time.time()
    output_from_network = network.forward(layers_names_output)
    end = time.time()

    # Showing spent time
    print('Objects Detection took {:.5f} seconds'.format(end - start))

    # Preparing lists for detected bounding boxes,
    # obtained confidences and class's number
    bounding_boxes = []
    confidences = []
    class_numbers = []

    for result in output_from_network:
        for detected_objects in result:
            # Getting all 80 classes' probabilities for current detected object
            scores = detected_objects[5:]
            # Getting index of the class with the maximum value of probability
            class_current = np.argmax(scores)
            # Getting value of probability for defined class
            confidence_current = scores[class_current]

            # Eliminating weak predictions with minimum probability
            if confidence_current > probability_minimum:
                box_current = detected_objects[0:4] * np.array([w, h, w, h])

                # Now, from YOLO data format, we can get top left corner coordinates
                x_center, y_center, box_width, box_height = box_current
                x_min = int(x_center - (box_width / 2))
                y_min = int(y_center - (box_height / 2))

                # Adding results into prepared lists
                bounding_boxes.append([x_min, y_min, int(box_width), int(box_height)])
                confidences.append(float(confidence_current))
                class_numbers.append(class_current)

    # Implementing non-maximum suppression of given bounding boxes
    results = cv2.dnn.NMSBoxes(bounding_boxes, confidences,
                               probability_minimum, threshold)

    # Defining counter for detected objects
    counter = 1
    cards = []
    if len(results) > 0:
        for i in results.flatten():
            # Showing labels of the detected objects
            print('Object {0}: {1}'.format(counter, labels[int(class_numbers[i])]))
            counter += 1
            print(labels[int(class_numbers[i])])

            # Getting current bounding box coordinates
            x_min, y_min = bounding_boxes[i][0], bounding_boxes[i][1]
            box_width, box_height = bounding_boxes[i][2], bounding_boxes[i][3]

            # Preparing colour for current bounding box
            # and converting from numpy array to list
            colour_box_current = colours[class_numbers[i]].tolist()

            # # # Check point
            # print(type(colour_box_current))  # <class 'list'>
            # print(colour_box_current)  # [172 , 10, 127]

            # Drawing bounding box on the original image
            cv2.rectangle(image_BGR, (x_min, y_min),
                          (x_min + box_width, y_min + box_height),
                          colour_box_current, 4)
            print('Coords: [', x_min, ',', y_min, ']')
            card = Card(labels[int(class_numbers[i])], x_min, y_min, picNumber)
            insert = True
            for c in cards:
                if c.suitNumber.__eq__(card.suitNumber):
                    insert = False

            if insert:
                cards.append(card)

            # Preparing text with label and confidence for current bounding box
            text_box_current = '{}: {:.4f}'.format(labels[int(class_numbers[i])],
                                                   confidences[i])

            # Putting text with label and confidence on the original image
            cv2.putText(image_BGR, text_box_current, (x_min, y_min - 5),
                        cv2.FONT_HERSHEY_COMPLEX, 1, colour_box_current, 3)

    # Comparing how many objects where before non-maximum suppression
    # and left after
    print()
    print('Total objects been detected:', len(bounding_boxes))
    print('Number of objects left after non-maximum suppression:', counter - 1)


    # Showing Original Image with Detected Objects
    if debug == 'yes':
        cv2.namedWindow('Detections', cv2.WINDOW_NORMAL)
        cv2.imshow('Detections', image_BGR)
        cv2.waitKey(0)
        cv2.destroyWindow('Detections')

    return cards
