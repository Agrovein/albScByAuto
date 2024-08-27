import imagehash
import pyautogui as pg
from getRandomCoordinates import *
from getRandomDuration import *
import time
import numpy as np
import pyscreenshot as ImageGrab
import cv2
import pytesseract
from PIL import Image, ImageOps
from coordinates import *


pytesseract.pytesseract.tesseract_cmd='C:/Program Files/Tesseract-OCR/tesseract.exe'

def fetchItemPrices(paymentCords):

    filename = 'Image.png'
    rawRecognizedText = ""
    pg.moveTo(getRandomCoordinates(cursorMoveCorde), duration=getRandomDuration())
    time.sleep(0.1)

    screen = np.array(ImageGrab.grab(bbox=(paymentCords)))
    cv2.imwrite(filename, screen)
    img = cv2.imread('Image.png')
    rawRecognizedText += pytesseract.image_to_string(img)

    itemPriceList = rawRecognizedText.split()
    #print(itemPriceList)
    return itemPriceList


def fetchCountAverage(tier, enchantement):

    t = int(tier)
    e = int(enchantement)

    if (t == 4 or t == 5) and (e == 0 or e == 1):
        point = count40
    else:
        point = zero

    filename = 'CountAverage.png'
    rawRecognizedText = ""
    time.sleep(0.1)
    pg.moveTo(soldItemsCursor, duration=getRandomDuration())
    time.sleep(0.3)

    screen = np.array(ImageGrab.grab(bbox=(point)))
    cv2.imwrite(filename, screen)
    img = cv2.imread('CountAverage.png')
    rawRecognizedText += pytesseract.image_to_string(img)
    count = rawRecognizedText.split()
    
    return count

def checkInventoryEmptiness():
    
    filename = 'EmptyCheck.png'
    pg.moveTo(getRandomCoordinates(cursorMoveCorde), duration=getRandomDuration())
    time.sleep(0.1)

    screen = np.array(ImageGrab.grab(bbox=(emptyInve)))
    cv2.imwrite(filename, screen)

    hash0 = imagehash.average_hash(Image.open('EmptyInv.png')) 
    hash1 = imagehash.average_hash(Image.open('EmptyCheck.png')) 
    cutoff = 5  # maximum bits that could be different between the hashes. 
    '''
    if hash0 - hash1 < cutoff:
        similar = 1
    else:
        similar = 0
    '''
    return hash0, hash1

def checkAmountFastBuy(cord):
    filename = 'afb.png'
    rawRecognizedText = ""
    pg.moveTo(getRandomCoordinates(cursorMoveCorde), duration=getRandomDuration())
    time.sleep(0.1)

    screen = np.array(ImageGrab.grab(bbox=(cord)))
    cv2.imwrite(filename, screen)
    img = cv2.imread('afb.png')
    rawRecognizedText += pytesseract.image_to_string(img, lang='eng', config="--psm 7")
    amount = rawRecognizedText.split()

    return amount

def checkQuality():
    filename = 'qual.png'
    rawRecognizedText = ""
    pg.moveTo(getRandomCoordinates(cursorMoveCorde), duration=getRandomDuration())
    time.sleep(0.1)

    screen = np.array(ImageGrab.grab(bbox=(717, 356, 810, 375)))
    cv2.imwrite(filename, screen)
    img = cv2.imread('qual.png')
    rawRecognizedText += pytesseract.image_to_string(img, lang='eng', config="--psm 7")
    quality = rawRecognizedText.split()
    return quality

def something():

    filename = 'rawr.png'
    rawRecognizedText = ""

    screen = np.array(ImageGrab.grab(bbox=(1095, 370, 1235, 440)))

    cv2.imwrite(filename, screen)
    img = cv2.imread('rawr.png')

    rawRecognizedText += pytesseract.image_to_string(img,config="--psm 7")
    itemPriceList = rawRecognizedText.split()

    return itemPriceList