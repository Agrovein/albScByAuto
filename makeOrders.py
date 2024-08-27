from screenFetching import *
import pyautogui
import keyboard
from deleteCommas import *
from coordinates import *

def crBuyOrder(amount, price):

    time.sleep(0.5)
    pyautogui.moveTo(amountOrderBuy, duration=getRandomDuration())
    pyautogui.leftClick()
    keyboard.write(str(amount))
    time.sleep(0.5)
    pyautogui.moveTo(getRandomCoordinates(priceOrder), duration=getRandomDuration())
    pyautogui.leftClick()
    keyboard.write(str(price+1))
    time.sleep(0.5)
    print(f"Buy order created with item amount: {amount}")
    return

def crSellOrder(price):
    cost = int(price)
    newCost = cost - 1
    pyautogui.moveTo(getRandomCoordinates(priceOrder), duration=getRandomDuration())
    pyautogui.leftClick()
    keyboard.write(str(newCost))
    time.sleep(0.2)
    return

def crFastBuyOrder():
    pyautogui.moveTo(getRandomCoordinates(buyOrderBTN_coordinates), duration=getRandomDuration())
    pyautogui.leftClick()
    time.sleep(0.3)
    pyautogui.moveTo(getRandomCoordinates(createOrderBtn), duration=getRandomDuration())
    pyautogui.leftClick()
    time.sleep(0.3)

    return