## use https://pythex.org/ to do online test
#\d : 0 - 9
#\D : NOT (0 - 9)
#\w : letter, number, "_"
#\W : NOT (letter, number, "_")
#\s : space, tab or newline
#\S : NOT (space, tab or newline)

import re  # RegEx library

def FindPhone():
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
    mo = phoneNumRegex.search('My number is 415-555-4242.')
    print('Phone number found: ' + mo.group())
    numRegex = re.compile(r'[1-5]')
    print(numRegex.search('My number is 415-555-4242.').group())

def FindPhoneWithParenthese():
    phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
    mo = phoneNumRegex.search('My number is 415-555-4242.')
    print('Phone number found: ' + mo.group(2))

def FindByPipe():
    heroRegex = re.compile(r"Batman|SpiderMan")
    print(heroRegex.search("Batman and SpiderMan").group())
    print(heroRegex.search("SpiderMan and Batman").group())

    heroRegex = re.compile(r"Bat(man|woman)") #Batman or Batwoman
    print(heroRegex.search("Batman, Batwoman and SpiderMan").group())
    print(heroRegex.search("SpiderMan and Batwoman").group())

    heroRegex = re.compile(r"Bat(wo)?man")  #(wo)? means wo is optional
    print(heroRegex.search("Batwoman, Batman and SpiderMan").group())

def MatchZeroOrMore():
    batRegex = re.compile(r'Bat(wo)*man') # (wo)* means match Zero or more.
    print(batRegex.search('The Adventures of Batwowowowoman').group())
    print(batRegex.search('The Adventures of Batman').group()) #OK

def MatchOneOrMore():    
    batRegex = re.compile(r'Bat(wo)+man') # (wo)+ means match at least one.
    print(batRegex.search('The Adventures of Batwoman').group())
    print(batRegex.search('The Adventures of Batman').group()) # ERROR

def MatchRepeat():
    batRegex = re.compile(r'(Hi){2}')
    print(batRegex.search('HiHi').group())
    #print(batRegex.search('Hi').group()) #ERROR
    greedyRegex = re.compile(r'(Hi){2,4}') # means HiHi, HiHiHi, HiHiHiHi
    print(greedyRegex.search('HiHiHi').group())
    nongreedyRegex = re.compile(r'(Hi){2,4}?') # add ? means match lower first
    print(nongreedyRegex.search('HiHiHi').group())

def FindAllMatch():
    phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # r means raw string
    print(phoneNumRegex.findall('Mobile number is 415-555-4242.'))
    print(phoneNumRegex.findall('Mobile number is 415-555-4242, Work number is 478-123-2424.'))

def FindStartEnd():
    startRegex = re.compile(r"^Start")
    print(startRegex.search("Start with abcd").group())
    endRegex = re.compile(r"End$")
    print(endRegex.search("Abc with End").group())

def FindIgnoreCase():
    regex = re.compile("KeNNeth", re.IGNORECASE)
    print(regex.search("Kenneth is a good man").group())

def ReplaceString():
    regex = re.compile("Karen")
    msg = "Karen is a good girl"
    print(msg)
    print(regex.sub("Yan", msg))

def Summary():
    print(r"re.compile(r'Bat(wo)+man')")
    print("? matches zero or one")
    print("* matches zero or more")
    print("+ matches one or more")
    print("".center(30, "*"))

    print(r"re.compile(r'(Hi){n}')")
    print(r"{n} match exactly n ")
    print(r"{n,} match n or more ")
    print(r"{,m} match 0 to m ")
    print(r"{n,m} match n to m ")
    print(r"{n,m}? match nongreedy (n first) ")
    print("".center(30, "*"))

    print(r"re.compile(r'^Start')")
    print(r"re.compile(r'End$')")
    print("".center(30, "*"))

    print(r"re.compile(r'[1-4]')")
    print(r"[1-4] match 1-4")
    print(r"[^1-4] not match 1-4")

#Summary()
#FindIgnoreCase()
ReplaceString()
#FindStartEnd()
#FindAllMatch()
#MatchRepeat()
#MatchOneOrMore()
#MatchZeroOrMore()
#FindByPipe()
#FindPhone()
#FindPhoneWithParenthese()