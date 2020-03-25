import threading, time

def takeANap(ann, ann1, ann2):
    time.sleep(5)
    print(ann)
    print('Wake up!!')

print("Start of program")
threadObj = threading.Thread(target=takeANap, args=['Cats', 'Dogs', 'Frogs'])
threadObj.start()

print("End of Program")