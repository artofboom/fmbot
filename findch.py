""" This script finds the pixel coordinates of the chs"""

import pyautogui
import defines

while True:
    pos = pyautogui.position()
    # color = pyautogui.screenshot(region=(pos[0]-20, pos[1]-20, pos[0], pos[1]))
    # color = color.getpixel((pos[0]-20, pos[1]-20))
    print(str(pos)) # + " " + str(color))
