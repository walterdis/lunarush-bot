from random import random
from time import sleep
from src import helper, fight, date
import pyautogui


def execute(screen):
    removeDepletedHeroes(screen)

    sleep(1)

    selectHeroes()
    startFight()


def removeDepletedHeroes(screen):
    heroesPositions = getSelectedHeroesDepletedPositions(screen)

    for (x, y, w, h) in heroesPositions:
        pyautogui.moveTo(x+100, y, 1 + random()/2)
        pyautogui.click()
        sleep(1)


def selectHeroes(screen=None):
    if(screen is None):
        screen = helper.printSreen()

    emptySlotPositions = getEmptySlotPositions(screen)
    emptySlotsAmount = len(emptySlotPositions)
    scrollAmount = 6

    if(emptySlotsAmount < 1):
        return

    hasOneHeroToFight = False
    while(emptySlotsAmount > 0):
        heroesPositions = getHeroesInListWithEnergyPositions(screen)
        for (x, y, w, h) in heroesPositions:
            if(emptySlotsAmount < 1):
                break

            pyautogui.moveTo(x+w/2, y+h/2-20, 1 + random()/2)
            pyautogui.click()
            hasOneHeroToFight = True

            emptySlotsAmount = emptySlotsAmount - 1
            sleep(1)

        if(scrollAmount < 1):
            break

        if(emptySlotsAmount < 1):
            break

        scrollHeroesList(screen)
        sleep(1)

        scrollAmount = scrollAmount - 1
        screen = helper.printSreen()

    if(hasOneHeroToFight is False):
        backToStageSelectAndWait()


def backToStageSelectAndWait():
    helper.clickDestination('btn-back-stage-select.png')
    print(date.dateFormatted(), ' Waiting for near 2 hours...')
    sleep(7000)


def startFight():
    helper.clickDestination('boss-hunt-button.png', 'boss-hunt')
    sleep(3)

    fight.execute(helper.printSreen())


def getEmptySlotPositions(screen):
    positions = helper.getImagePositions(
        'hero-select-empty-slot.png', 0.9, screen)

    print('Empty Slots: ', len(positions))
    return positions


def getHeroesInListWithEnergyPositions(screen):
    positions = helper.getImagePositions(
        'hero-list-has-energy.png', 0.9, screen)

    print('Heroes with energy: ', len(positions))
    return positions


def getHeroesInListWithDepletedEnergyPositions(screen):
    positions = helper.getImagePositions(
        'hero-list-depleted-energy.png', 0.9, screen)

    print('heroes no energy: ', len(positions))
    return positions


def getSelectedHeroesDepletedPositions(screen):
    positions = helper.getImagePositions(
        'hero-select-depleted-energy.png', 0.9, screen)

    print('selected heroes no energy: ', len(positions))
    return positions


def scrollHeroesList(screen):
    startScrollPosition = helper.getImagePositions(
        'hero-select-warrior-text.png', 0.9, screen)

    if(len(startScrollPosition) < 1):
        print('Position to scroll heroes not found!!!')
        return False

    x, y, w, h = startScrollPosition[0]

    pyautogui.moveTo(x+50, y+100, 1)
    pyautogui.dragRel(0, -150, duration=1, button='left')

    return
