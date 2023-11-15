import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

from typing import Dict

SIZE_MAP = (600, 600, 3)   # x, y
CENTER = (SIZE_MAP[0] //2, SIZE_MAP[1] //2)
RADIUS = SIZE_MAP[0] //2

DELTA = 360 //45

def getColors():

    colors = []

    colors.append((255, 0, 0))
    colors.append((242, 255, 0))
    colors.append((26, 255, 0))
    colors.append((0, 255, 221))
    colors.append((0, 106, 255))
    colors.append((140, 0, 255))
    colors.append((255, 0, 242))

    return colors

def getAlphabet():

    alphabet = {}   # key -> symbol, value -> color
    colors = getColors()
    qColors = len(colors)

    colorCounter = 0
    for i in range(65, 91):
        alphabet[chr(i)] = ((colors[qColors - colorCounter //qColors - 1]), (colors[colorCounter %qColors]))
        colorCounter += 1

    alphabet[" "] = ((255, 255, 255), (255, 255, 255))

    return alphabet

def drawCode(map, msg: str, alphabet):

    angle = 0
    angleMessage = 2 * DELTA * len(msg)
    
    while angle < 360:

        map = cv.ellipse(map, CENTER, (RADIUS, RADIUS), 0, angle, angle + DELTA, alphabet[msg[angle % angleMessage // (2*DELTA)]][0], -1)
        angle += DELTA

        map = cv.ellipse(map, CENTER, (RADIUS, RADIUS), 0, angle, angle + DELTA, alphabet[msg[(angle -8) % angleMessage // (2*DELTA)]][1], -1)
        angle += DELTA

    return map

msg = "SCANDALIST "#input("Message: ")

alphabet = getAlphabet()

map = np.zeros(shape=SIZE_MAP, dtype='uint8')

map = cv.rectangle(map, (0, 0), (SIZE_MAP[0], SIZE_MAP[1]), (220, 200, 200), -1)

map = cv.circle(map, CENTER, RADIUS, (255, 255, 255), -1)

map = drawCode(map, msg, alphabet)

cv.imwrite("demo/code.png", map)

cv.namedWindow("Map")

cv.imshow("Map", map)
k = cv.waitKey(0)