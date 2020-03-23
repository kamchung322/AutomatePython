# https://pyinputplus.readthedocs.io/.
# Full Documentation
import pyinputplus as pyip

def InputNumber():
    response = pyip.inputNum("Please input number")

def InputNumberRange():
    response = pyip.inputNum("Please input number", min=3, max=100)

def InputNonEven():
    #ERROR
    response = pyip.inputNum(blockRegexes=[r'[02468]$'])

#InputNumber()
#InputNumberRange()
#InputNonEven()