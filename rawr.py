import time
import datetime
import gspread
import imagehash
from getRandomCoordinates import *
from getRandomDuration import *
from coordinates import *
import pyautogui as pg
import cv2
import numpy as np
import pyscreenshot as ImageGrab
from PIL import Image
import math


print(math.floor(10*10/5))


'''
#checking if inventory empty
filename = 'EmptyCheck.png'
rawRecognizedText = ""
pg.moveTo(getRandomCoordinates(cursorMoveCorde), duration=getRandomDuration())
time.sleep(0.1)

screen = np.array(ImageGrab.grab(bbox=(emptyInve)))
cv2.imwrite(filename, screen)

hash0 = imagehash.average_hash(Image.open('EmptyInv.png')) 
hash1 = imagehash.average_hash(Image.open('EmptyCheck.png')) 
cutoff = 5  # maximum bits that could be different between the hashes. 

if hash0 - hash1 < cutoff:
  print('images are similar')
else:
  print('images are not similar')

'''