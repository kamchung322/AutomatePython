
def RawString():
    print(r"I\'m raw string")
    print("I\'m not raw string")
    print("I'm not raw string")

def TripleQuote():
    print('''Dear Alice,
Eve's cat has been arrested for catnapping, cat burglary, and extortion.
Sincerely,
Bob''')

def MultilineComment():
    """
    Using triple "double" quota to do multi-line comment
    I'm multi-line comment
    """

def Manipulate():
    spam = 'Have a nice day'
    print(spam[0])
    print(spam[:3])
    print(spam[3:-2])
    print(spam[5:])

def Instr():
    msg = "Have a nice day"
    print("Have" in msg)
    print("Good" in msg)
    print(msg.startswith("Today"))
    print(msg.endswith("day"))

def PutString():
    name = "Kenneth"
    msg = "%s, have a nice day" %name
    print(msg)
    name = "Karen"
    msg = f"In Python 3.6, {name}, have a nice day"
    print(msg)

def Joining():
    msg = "Today is a good day"
    print(",".join(["A", "B", "C"]))

def Spliting():
    msg = "Today is a good day"    
    print(msg.split())
    print(msg.split("o"))
    print(msg.partition("o"))
    before, sep, after = msg.partition("o")
    print("Before : %s, Sep : %s, After : %s" %(before, sep, after))

def Padding():
    msg = "Today is a good day"
    print("rjust(30) : %s" %msg.rjust(30))
    print("ljust(30) : %s" %msg.ljust(30, "*"))
    print("center(30) : %s" %msg.center(30, "*"))

def Striping():
    msg = "    Today is a good day    "
    print("rstrip : '%s'" %msg.rstrip())
    print("lstrip : '%s'" %msg.lstrip())
    print("strip : '%s'" %msg.strip())
    spam = 'SpamSpamBaconSpamEggsSpamSpam'
    print(spam.strip('ampS')) # strip with 'a', 'm', 'p', 'S'
    print(spam.strip('Spam')) # order doesn't matter

def AsciiCode():
    print("ord('A') : %s" %ord('A'))
    print("chr('70') : %s" %chr(70))

AsciiCode()
#Striping()
#Joining()
#Padding()
#Spliting()
#PutString()
#Instr()
#Manipulate()
#MultilineComment()
#TripleQuote()
#RawString()