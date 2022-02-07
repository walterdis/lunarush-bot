# -*- coding: utf-8 -*-
from cv2 import cv2

from os import listdir
from random import randint, uniform
from random import random

import numpy as np
import pyautogui
import time
import sys
from src import login, helper, bosshunt, heroselect, fight, date


#pyautogui.PAUSE = pause
pyautogui.FAILSAFE = False


def main():

    time.sleep(1)

    while True:
        now = time.time()

        screen = helper.printSreen()
        if(isLoginScreen(screen)):
            print('Login screen found!!!')
            login.doLogin()

        screen = helper.printSreen()
        if(isModeSelectScreen(screen)):
            print('Mode select found!!!')
            helper.clickDestination('boss-fight-mode-icon.png', 'boss-fight-mode')

        screen = helper.printSreen()
        if(isBossHuntStageSelect(screen)):
            print('Boss stage select screen found!!!')
            bosshunt.execute()

        screen = helper.printSreen()
        if(isHeroSelectScreen(screen)):
            print('Hero select screen found!!!')
            heroselect.execute(screen)

        screen = helper.printSreen()
        fight.execute(screen)

        sys.stdout.flush()

        print('waiting ...')
        time.sleep(1)


def isLoginScreen(screen):
    positions = helper.getImagePositions('connect-wallet.png', 0.7, screen)

    return len(positions) > 0


def isModeSelectScreen(screen):
    positions = helper.getImagePositions(
        'boss-fight-mode-icon.png', 0.7, screen)

    return len(positions) > 0


def isModeSelectScreen(screen):
    positions = helper.getImagePositions(
        'boss-fight-mode-icon.png', 0.7, screen)

    return len(positions) > 0


def isBossHuntStageSelect(screen):
    positions = helper.getImagePositions('boss-hunt-map.png', 0.7, screen)

    return len(positions) > 0


def isHeroSelectScreen(screen):
    positions = helper.getImagePositions('boss-hunt-button.png', 0.7, screen)

    return len(positions) > 0


main()