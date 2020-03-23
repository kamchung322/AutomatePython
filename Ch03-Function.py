import random

def numToWeekday(num):
    if num == 1:
        return "Monday"
    elif num == 2:
        return "Tuesday"
    elif num == 3:
        return "Wednesday"
    elif num == 4:
        return "Thursday"
    elif num == 5:
        return "Friday"
    elif num == 6:
        return "Saturday"
    elif num == 7:
        return "Sunday"

for i in range(5):
    w = random.randint(1,7)
    print(numToWeekday(w))

