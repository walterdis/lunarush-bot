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

wolf = """
                                                                  .
                                                                 / V\\
                                                               / `  /
                                                              <<   |
                                                              /    |
                                                            /      |
                                                          /        |
                                                        /    \  \ /
                                                       (      ) | |
                                               ________|   _/_  | |
                                             <__________\______)\__)
=========================================================================
======================== LUS BUSD BNB USDT USDC =========================
============== 0x1F66230C4e98b557D3e55d7d2C047CcbA8E55bD6 ===============
=========================================================================
============== https://github.com/walterdis/lunarush-bot ================
=========================================================================
"""


print(wolf)
time.sleep(4)

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
            helper.clickDestinationImage('boss-fight-mode-icon.png', 'boss-fight-mode')
            time.sleep(2)

        screen = helper.printSreen()
        if(isBossHuntStageSelect(screen)):
            print('Boss stage select screen found!!!')
            bosshunt.execute()
            time.sleep(2)

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