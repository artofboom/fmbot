""" This script moves through fm and takes screenshots of every item
in fm for later evaluation by ocr."""
import time
import pyautogui

from char import Char
import defines


# make mule
time.sleep(0.1)
pyautogui.click(400, 100)
fmmule = Char()
# fmmule.getCurrentChannel()
# fmmule.goToFm()
# fmmule.moveCharToTheLeftOfFM()
# fmmule.checkFmLudi()
fmmule.checkStoresLudi()

#while True:
#    pixel = fmmule.checkIfMapChanges()
#    if (all(i < j for i, j in zip(pixel, defines.black))):
#            print(pixel)
print("DONE")

