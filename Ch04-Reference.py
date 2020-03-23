import copy

def fun1():
    str1 = "abc"
    print(id(str1))
    str1 = "def"
    print(id(str1))
    print("id show the location of memory")

def eggs(someParameter):
    print(id(someParameter))
    someParameter.append('Hello')

def passByRef():
    spam = [1, 2, 3]
    print(id(spam))
    eggs(spam)
    print(spam)

def copyByVal():
    spam = [1, 2, 3]
    spam2 = copy.copy(spam)
    print('Spam Id (%s), Spam2 Id (%s)' %(id(spam), id(spam2)))

def copyByRef():
    spam = [1, 2, 3]
    spam2 = spam
    print('Spam Id (%s), Spam2 Id (%s)' %(id(spam), id(spam2)))

copyByRef()
#copyByVal()
#passByRef()
