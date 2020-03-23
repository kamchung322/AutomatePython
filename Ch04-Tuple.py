


def tupleIsImmutable():
    tupleList = ('hello', 32, 0.4)
    print(tupleList[0])
    try:
        tupleList[0] = "How are you?"
    except:
        print("Tuple is immutable !!")

def tupleClass():
    tuple2 = ('hello',)
    print(type(tuple2))
    print("Add , at the end of () will turn to tuple")
    str2 = ('hello')
    print(type(str2))

def conversion():
    print(tuple(['cat', 'dog', 5]))
    print(list(('cat', 'dog', 5)))
    print(list('hello'))
    print(tuple('hello'))

conversion()