myCat = {'size': 'fat', 'color': 'gray'}

def Basic():

    print("Size is %s" %myCat['size'])
    myCat['dispo'] = 'loud'
    print("Dispo is %s" %myCat['dispo'])

def loopKey():
    for k in myCat.keys():
        print("Key is %s" %(k))

def loopValue():
    for v in myCat.values():
        print("Value is %s" %(v))

def loopItem():
    for i in myCat.items():
        print(i)

def printKey():
    print(myCat.keys())
    print(list(myCat.keys()))

def checkValueExistDict():
    isExist = 'size' in myCat.keys()
    print(isExist)
    isExist = 'size' in myCat.values()
    print(isExist)
    isExist = 'size' not in myCat.keys()
    print(isExist)
    isExist = 'size' in myCat
    print(isExist)

def getValueFromDict():
    print("Get size : %s" %(myCat.get('size')))
    print("Get height : %s" %(myCat.get('height')))

def setDefaultDict():
    print('Before set : %s' %(myCat.get('Age')))
    myCat.setdefault('Age', 10)
    print('After set : %s' %(myCat.get('Age')))
    myCat.setdefault('Age', 20)
    print('Set again : %s' %(myCat.get('Age')))

def wordCount():
    message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
    count = {}

    for character in message:
        count.setdefault(character, 0)
        count[character] = count[character] + 1

    print(count)    

wordCount()
#setDefaultDict()
#getValueFromDict()
#checkValueExistDict()
#printKey()
#loopItem()
#loopValue()
#loopKey()
#Basic()