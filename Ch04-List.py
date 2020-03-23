import random
spam = [1,2,3,4,5,"ABC"]

def displayList(header, spamList):
    print(header, end=" : ")
    for i in spamList:
        print (i, end=", ")

def displayNegativeList():
    print("displayNegativeList " + str(spam[-3]))

def sliceList():
    displayList("SliceList", spam[2:-1])

def displayLenOfList():
    print("Lenght : " + str(len(spam)))

def editList():
    print("Edit List")
    displayList("Original List", spam)
    print("")
    spam[3] = "Changed"
    displayList("New List", spam)

def catList():
    global spam
    print("Cat List")
    displayList("Original List", spam)
    print("")
    spam = spam + ["n1", "n2", "n3"]
    displayList("New List", spam)

def displayMatrix():
    matrixList = [["A","B","C"],["D","E","F"]]
    print("Matrx[0] : " + str(matrixList[0]))
    print("Matrix[0][2] : " + str(matrixList[0][2]))
    print("Matrix[1][2] : " + str(matrixList[1][2]))

def delList():
    print("Delete List")
    displayList("Original List", spam)
    print("")
    del spam[2]
    displayList("New List", spam)

def removeList():
    animal = ["Cat", "Dog", "Mouse", "Cat"]
    animal.remove("Cat")
    displayList("Remove List", animal)

def dynamicInputList():
    numList = []
    for i in range(5):
        numList = numList + [i]
    numList = numList + ["Eof"]
    print("Dynamic Input List")
    displayList("List", numList)

def displayInNotInList():
    nameList = ["Kenneth", "Karen", "Yan", "Amy"]
    isInList = "Kenneth" in nameList
    print("Kenneth is in List = " + str(isInList))
    isInList = "May" in nameList
    print("May is in List = " + str(isInList))

def multiAssignList():
    animal = ["Cat", "Dog", "Mouse"]
    a = animal[0]
    b = animal[1]
    c = animal[2]
    print("%s, %s, %s" %(a,b,c))
    a,b,c = animal
    print("%s, %s, %s" %(a,b,c))

def enumerateList():
    nameList = ["Kenneth", "Karen", "Yan", "Amy"]
    for i, name in enumerate(nameList):
        print("Item %s, Name is %s" %(i,name))

def randomChoiceList():
    print("Random Choice : %s" %random.choice(spam))
    print("Random Choice : %s" %random.choice(spam))
    print("Random Choice : %s" %random.choice(spam))

def shuffleList():
    print("Shuffle List")
    displayList("Original List", spam)
    print("")
    random.shuffle(spam)
    displayList("New List", spam)

def appendList():
    numList = [1,2,3,4,5]
    numList.append(6)
    displayList("Append List", numList)

def insertList():
    numList = [1,2,3,4,5]
    numList.insert(3,6)
    displayList("Insert List", numList)

def sortList():
    numList = [1,3,5,2,4]
    numList.sort()
    displayList("Sort Asc", numList)
    numList.sort(reverse=True)
    displayList("Sort Desc", numList)
    numList.reverse()
    displayList("Reverse", numList)

def reverseList():
    numList = [1,3,5,2,4]
    numList.reverse()
    displayList("Reverse", numList)

#reverseList()
#sortList()
removeList()
#delList()
#appendList()
#insertList()
#shuffleList()
#randomChoiceList()
#enumerateList()
#multiAssignList()
#displayInNotInList()
#dynamicInputList()
#displayList("Display", spam)
#displayNegativeList()
#sliceList()
#displayLenOfList()
#editList()
#catList()
#displayMatrix()
