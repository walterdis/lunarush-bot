from random import random, uniform
from src import helper
import pyautogui

def execute():
    mapSelect(helper.printSreen())


def isLastStageLockedShowing(screen):
    positions = helper.getImagePositions(
        'boss-stage-last-locked.png', 0.9, screen)

    return len(positions) > 0


def selectAvailableStage(screen):
    availableStagePosition = helper.getImagePositions(
        'boss-select-green.png', 0.9, screen)

    if(len(availableStagePosition) < 1):
        return False

    helper.clickDestinationImage(
        'boss-select-green.png', 'select-stage', 3, 0.9)

    return True


def scrollLastCompletedStagePosition():
    screen = helper.printSreen()

    completedStagesPositions = helper.getImagePositions(
        'boss-select-yellow.png', 0.9, screen)

    if(len(completedStagesPositions) < 1):
        print('completed stages not found')
        return False

    positionsLen = len(completedStagesPositions) - 1

    x, y, w, h = completedStagesPositions[positionsLen]

    #pyautogui.moveTo(x+100, y, 1+random()/2)

    pos_x = int(x+uniform(100, 120))
    pos_y = int(y+uniform(5, 20))

    helper.moveDestination(pos_x, pos_y, 2)
    pyautogui.dragRel(-150, 0, duration=2, button='left')

    return


def mapSelect(screen):
    while(True):
        if(selectAvailableStage(screen)):
            print('Available boss found!!!')
            break

        if(isLastStageLockedShowing(screen)):
            print('Last stage found but no available stages to fight!')
            break

        if(scrollLastCompletedStagePosition()):
            continue
