import shelve, pprint

def SaveBinaryFormat():
    shelfFile = shelve.open('ShelveFile')
    cats = ['Zophie', 'Pooka', 'Simon']
    shelfFile['catcat'] = cats
    shelfFile.close()

def ReadBinaryFormat():
    shelfFile = shelve.open('ShelveFile')
    pprint.pprint(list(shelfFile.keys()))
    pprint.pprint(list(shelfFile.values()))  #pprint.pprint => console
    strShelf = pprint.pformat(list(shelfFile.values())) # pprint.pformat => text
    print(shelfFile['cats'])
    shelfFile.close()

SaveBinaryFormat()
ReadBinaryFormat()

