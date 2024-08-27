import time
import pyautogui

#tool for coordinates finding
time.sleep(2)
print('x1y1')
left_top = pyautogui.position()
print(left_top)
time.sleep(2)
print('x2y2')
right_bottom = pyautogui.position()
print(right_bottom)