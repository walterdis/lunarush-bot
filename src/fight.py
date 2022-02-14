from random import random, uniform
import time
from src import helper
import pyautogui


def execute(screen):
    if(isFighting(screen)):
        handleFight()

    handleResultScreen(screen)


def handleFight():
    clicksAmount = 0
    while(True):
        screen = helper.printSreen()
        clicksAmount = clicksAmount + 1
        bossIconPosition = getBossIconPosition(screen)
        versusIconPosition = getVersusIconPosition(screen)

        if(len(bossIconPosition) < 1 and len(versusIconPosition) < 1):
            handleResultScreen(helper.printSreen())
            break

        # @TODO fix this workaround to prevend error
        if(len(versusIconPosition) < 1):
            break

        x, y, w, h = versusIconPosition[0]
        #pyautogui.moveTo(x, y+300,  1 + random()/2)

        pos_x = int(x+uniform(-150, 150))
        pos_y = int(y+uniform(100, 200))

        helper.moveDestination(pos_x, pos_y)
        pyautogui.click()

        print('Fight click ', clicksAmount)

        if(clicksAmount > 15):
            pyautogui.hotkey('ctrl', 'f5')
            break

        time.sleep(2+uniform(1, 5.5))


def handleResultScreen(screen):
    resultTapOpen = helper.getImagePositions(
        'result-tap-to-open.png', 0.8, screen)

    if(len(resultTapOpen) > 0):
        x, y, w, h = resultTapOpen[0]
        
        pos_x = int(x+uniform(10, 20))
        pos_y = int(y+uniform(10, 20))

        #pyautogui.moveTo(x+10, y+10,  0.5 + random()/2)
        helper.moveDestination(pos_x, pos_y)

        pyautogui.click()
        time.sleep(5)

    resultEnergy = helper.getImagePositions(
        'result-screen-energy.png', 0.8)

    if(len(resultEnergy) < 1):
        return

    x, y, w, h = resultEnergy[0]
    
    pos_x = int(x+uniform(50, 80))
    pos_y = int(y+uniform(50, 100))

    #pyautogui.moveTo(x, y+50,  0.5 + random()/2)
    
    helper.moveDestination(pos_x, pos_y)
    pyautogui.click()


def getVersusIconPosition(screen):
    position = helper.getImagePositions('fight-versus.png', 0.6, screen)
    print('Versus Icon Position: ', len(position))

    return position


def getBossIconPosition(screen):
    position = helper.getImagePositions('fight-boss-icon.png', 0.7, screen)
    print('Boss Icon Position: ', len(position))

    return position


def isFighting(screen):
    bossIconPosition = getBossIconPosition(screen)
    versusIconPosition = getVersusIconPosition(screen)

    if(len(bossIconPosition) < 1 and len(versusIconPosition) < 1):
        return False

    return True
