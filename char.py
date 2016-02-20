import pyautogui
import time


import defines
pyautogui.PAUSE = defines.pause
pyautogui.FAILSAFE = defines.failsafe


class Char:
    def init(self, currentchannel=None):
        if currentchannel is None:
            currentchannel = self.getCurrentChannel()
        self.currentchannel = currentchannel

    def getCurrentChannel(self):
        """Finds the ch the char is currently in"""
        pyautogui.typewrite(['esc'])
        time.sleep(0.5)
        pyautogui.typewrite(['enter'])
        time.sleep(0.5)
        im = pyautogui.screenshot(region=(0, 0, 800, 600))
        for key in defines.ch.keys():
            if im.getpixel(defines.ch[key])[2]-im.getpixel(
                    defines.ch[key])[0] > 100:
                self.currentchannel = key
                print("Currently in ch " +
                      str(self.currentchannel))
                pyautogui.typewrite(['esc'])
                time.sleep(0.5)
                return True
        throw(RuntimeError)

    def getCharPos(self):
        """Returns char position based on the minimap"""
        # return pyautogui.locateCenterOnScreen('pics/CharMinimapIcon.png')

    def moveCharToTheLeftOfFM(self):
        CharIsLeft = False
        pyautogui.keyDown('left')
        while not CharIsLeft:
            im = pyautogui.screenshot(region=(0, 0, 800, 600))
            left = im.getpixel((9, 138))
            if 212 < left[0] and left[0] < 224:
                if 200 < left[1] and left[1] < 208:
                    if 14 < left[2] and left[2] < 18:
                        CharIsLeft = True
        pyautogui.keyUp('left')

    def changeChannel(self, channel):
        """Changes channels"""
        # TODO add checks for breathing
        if 0 < channel and channel < 13:
            if channel == self.currentchannel:
                return True
            pyautogui.typewrite(['esc'])
            time.sleep(0.5)
            pyautogui.typewrite(['enter'])
            time.sleep(0.5)
            pyautogui.click(defines.ch[channel][0],
                            defines.ch[channel][1],
                            duration=0.25)
            pyautogui.typewrite(['enter'])
            return True
        else:
            throw(ValueError)

    def goToFm(self):
        pyautogui.click(defines.fm[0], defines.fm[1], duration=0.25)

    def checkFmLudi(self):
        self.goToFm7()
        self.checkclickStoresLudi()

    def goToFm7(self):
        """requires you to be left first in fm."""
        CharIsLeft = False
        im = pyautogui.screenshot(region=(0, 0, 800, 600))
        left = im.getpixel((9, 138))
        if 212 < left[0] and left[0] < 224:
            if 200 < left[1] and left[1] < 208:
                if 14 < left[2] and left[2] < 18:
                    CharIsLeft = True
        assert(CharIsLeft)
        reachedGoal = False
        pyautogui.keyDown('right')
        time.sleep(2)
        pyautogui.keyDown('up')
        while not reachedGoal:
            color = self.checkIfMapChanges()
            print(color)
            reachedGoal = all(i < j for i, j in zip(color, defines.black))
        pyautogui.keyUp('up')
        pyautogui.keyUp('right')

    def goToFm1(self):
        """requires you to be left first in fm."""
        CharIsLeft = False
        im = pyautogui.screenshot(region=(0, 0, 800, 600))
        left = im.getpixel((9, 138))
        if 212 < left[0] and left[0] < 224:
            if 200 < left[1] and left[1] < 208:
                if 14 < left[2] and left[2] < 18:
                    CharIsLeft = True
        assert(CharIsLeft)
        reachedGoal = False
        pyautogui.keyDown('right')
        pyautogui.keyDown('up')
        while not reachedGoal:
            color = self.checkIfMapChanges()
            print(color)
            reachedGoal = all(i < j for i, j in zip(color, defines.black))
        pyautogui.keyUp('up')
        pyautogui.keyUp('right')

    def checkStoresLudi(self):
        storeOpen = False
        while not storeOpen:
            pyautogui.click(clicks=2, x=370, y=370)
            im = pyautogui.screenshot(region=(620, 300, 621, 301))
            color = im.getpixel((0, 0))
            storeOpen = all(i > j for i, j in zip(color, defines.white))
            self.checkStore()

    def checkStore():
        # 300, 230
        pyautogui.moveTo(300, 230, duration=0.1)
        pyautogui.moveTo(301, 231, duration=0.1)
        pyautogui.moveTo(300, 230, duration=0.1)
        im = pyautogui.screenshot(region=0, 0, 800, 600)

    def checkStoresHenesys(self):
        pass

    def checkIfMapChanges(self):
        im = pyautogui.screenshot(region=(400, 365, 401, 366))
        return(im.getpixel((0, 0)))
