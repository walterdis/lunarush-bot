from src import helper
import pyautogui


def execute():
    mapSelect(helper.printSreen())


def isLastStageLockedShowing(screen):
    positions = helper.getImagePositions(
        'boss-stage-last-locked.png', 0.7, screen)

    return len(positions) > 0


def selectAvailableStage(screen):
    availableStagePosition = helper.getImagePositions(
        'boss-select-green.png', 0.9, screen)

    if(len(availableStagePosition) < 1):
        return False

    helper.clickDestination('boss-select-green.png', 'select-stage', 3, 0.9)

    return True


def scrollLastCompletedStagePosition(screen):
    completedStagesPositions = helper.getImagePositions(
        'boss-select-yellow.png', 0.9, screen)

    if(len(completedStagesPositions) < 1):
        print('completed stages not found')
        return False

    positionsLen = len(completedStagesPositions) - 1

    x, y, w, h = completedStagesPositions[positionsLen]

    pyautogui.moveTo(x+100, y, 1)
    pyautogui.dragRel(-200, 0, duration=1, button='left')

    return


def mapSelect(screen):
    while(True):
        if(selectAvailableStage(screen)):
            print('Available boss found!!!')
            break

        if(isLastStageLockedShowing(screen)):
            print('Last stage found but no available stages to fight!')
            break

        if(scrollLastCompletedStagePosition(screen)):
            continue
