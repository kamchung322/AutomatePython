# move mouse point to corner if program fail
# https://automatetheboringstuff.com/2e/chapter20/
# Good for manipulate keyboard, mouse, 

import pyautogui

def displayResolution():
    wh = pyautogui.size()
    print(wh)

displayResolution()

def moveMouseToAbsPosition():
    for i in range(10):
        pyautogui.moveTo(100,100,duration=0.25)
        pyautogui.moveTo(200,100,duration=0.25)
        pyautogui.moveTo(200,200,duration=0.25)
        pyautogui.moveTo(100,200,duration=0.25)

def moveMouseToRelative():
    for i in range(10):
        pyautogui.move(100,0,duration=0.25)
        pyautogui.move(0,100,duration=0.25)
        pyautogui.move(-100,0,duration=0.25)
        pyautogui.move(0,-100,duration=0.25)

def screenShot():
    im = pyautogui.screenshot()

def displayMsgBox():
    pyautogui.alert("This is alert!!!")
    pyautogui.confirm('Do you want to continue?') 
    pyautogui.prompt("What is your cat's name?")
    pyautogui.password('What is the password?')

displayMsgBox()
#screenShot()
#moveMouseToRelative()
#moveMouseToAbsPosition()
