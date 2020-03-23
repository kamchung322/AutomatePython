while True:
    print('Pls input Kenneth to exit program')
    yourName = input('What is your name?')
    if yourName == 'Kenneth':
        print('%s, You are so smart' %(yourName))
        break  # exit the while 
    elif yourName == "Yan":
        print('You are a good girl')
        continue # return to the start of the while
    else:
        print('Nice to meet you, ' + yourName)
    print('hihi')

#print('Thank you, you will exit the program')
#
#for i in range(5,0,-1):
#    print("Will be exit after " + str(i))