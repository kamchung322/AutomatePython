import traceback, logging

def raiseException():
    try:
        print("Before raise exception")
        raise Exception("Raise exception manually")
    except Exception as ex:
        print(ex)

def displayTraceback():
    try:
        print("Before raise exception")
        raise Exception("Raise exception manually")
    except Exception as ex:
        print(traceback.format_exc())

def assertion():
    ages = [4,5,6,7,8,1]
    ages.sort()
    print("assert means if the condition is true, no error raise")
    print("Assertions are for programmer errors, not user errors")
    assert ages[0] <= ages[-1], "message"
    ages.reverse()
    assert ages[0] <= ages[-2], "message"

def logInformation():
    # default print to console
    #logging.basicConfig(level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
    # logging to file
    logging.basicConfig(filename="loginfo.txt", level=logging.DEBUG, format=' %(asctime)s -  %(levelname)s -  %(message)s')
    logging.debug("Start Program")
    logging.info("I'm logging.info")
    print("I'm print")
    logging.debug("End Program")

logInformation()
#assertion()
#displayTraceback()
#raiseException()

