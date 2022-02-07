from random import random
import cv2
import mss
import time
import numpy as np
import pyautogui

def clickDestination(img, name=None, timeout=3, threshold=0.7):
    if not name is None:
        pass

    start = time.time()
    while(True):
        matches = getImagePositions(img, threshold)
        if(len(matches) == 0):
            has_timed_out = time.time()-start > timeout
            if(has_timed_out):
                return False

            continue

        x, y, w, h = matches[0]
        pos_click_x = x+w/2
        pos_click_y = y+h/2

        pyautogui.moveTo(pos_click_x, pos_click_y, 1 + random()/2)
        pyautogui.click()

        return True


def getImage(filename):
    path = 'target_images/' + filename

    return cv2.imread(path)


def getImagePositions(imageName, threshold=0.7, img=None):
    if img is None:
        img = printSreen()

    target = getImage(imageName)

    result = cv2.matchTemplate(img, target, cv2.TM_CCOEFF_NORMED)
    w = target.shape[1]
    h = target.shape[0]

    yloc, xloc = np.where(result >= threshold)

    rectangles = []
    for (x, y) in zip(xloc, yloc):
        rectangles.append([int(x), int(y), int(w), int(h)])
        rectangles.append([int(x), int(y), int(w), int(h)])

    rectangles, weights = cv2.groupRectangles(rectangles, 1, 0.2)

    return rectangles


def printSreen():
    with mss.mss() as sct:
        monitor = sct.monitors[0]
        sct_img = np.array(sct.grab(monitor))

        return sct_img[:, :, :3]
