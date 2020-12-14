hand = input("Input your hand: ")
hand = hand.replace(",", "", 4)
hand = hand.replace("10", "X")
hand = list(hand)
points = 0
nextCheck = False
counter = 0
string = ""
numList = []
for i in hand:
    if i == ("A") or i == ("2") or i == ("3") or i == ("4") or i == ("5") or i == ("6") or i == ("7") or i == ("8") or i == ("9") or i == ("X") or i == ("J") or i == ("Q") or i == ("K"):
        numList.append(i)
counter = 0
for i in numList:
    if i == ("J"):
        numList[counter] = i.replace("J", "11")
    counter = counter + 1
counter = 0
for i in numList:
    if i == ("Q"):
        numList[counter] = i.replace("Q", "12")
    counter = counter + 1
counter = 0
for i in numList:
    if i == ("K"):
        numList[counter] = i.replace("K", "13")
    counter = counter + 1
counter = 0
for i in numList:
    if i == ("A"):
        numList[counter] = i.replace("A", "1")
    counter = counter + 1
counter = 0
for i in numList:
    if i == ("X"):
        numList[counter] = i.replace("X", "10")
    counter = counter + 1
numList = [int(i) for i in numList]
numList.sort()
numList = [str(i) for i in numList]
print(numList)
numList = numList[0] + numList[1] + numList[2] + numList[3] + numList[4]
print(numList)

def run(numList, points):
    if numList.find("123") != 0:
        if numList.find("1234") != 0:
            if numList.find("12345") != 0:
                points = points + 5
            else:
                points = points + 4
        else:
            points = points + 3
    elif numList.find("234") != 0:
        if numList.find("2345") !=0:
            if numList.find("23456") != 0:
                points = points + 5
            else:
                points = points + 4
        else:
            points = points + 3
    elif numList.find("345") != 0:
        if numList.find("3456") !=0:
            if numList.find("34567") != 0:
                points = points + 5
            else:
                points = points + 4
        else:
            points = points + 3
    elif numList.find("456") != 0:
        if numList.find("4567") !=0:
            if numList.find("45678") != 0:
                points = points + 5
            else:
                points = points + 4
        else:
            points = points + 3
    elif numList.find("567") != 0:
        if numList.find("5678") !=0:
            if numList.find("56789") != 0:
                points = points + 5
            else:
                points = points + 4
        else:
            points = points + 3
    elif numList.find("678") != 0:
        if numList.find("6789") !=0:
            if numList.find("678910") != 0:
                points = points + 5
            else:
                points = points + 4
        else:
            points = points + 3
    elif numList.find("789") != 0:
        if numList.find("78910") !=0:
            if numList.find("7891011") != 0:
                points = points + 5
            else:
                points = points + 4
        else:
            points = points + 3
    elif numList.find("8910") != 0:
        if numList.find("891011") !=0:
            if numList.find("89101112") != 0:
                points = points + 5
            else:
                points = points + 4
        else:
            points = points + 3
    elif numList.find("91011") != 0:
        if numList.find("9101112") !=0:
            if numList.find("910111213") != 0:
                points = points + 5
            else:
                points = points + 4
        else:
            points = points + 3
    elif numList.find("101112") != 0:
        if numList.find("10111213") != 0:
            points = points + 4
        else:
            points = points + 3
    elif numList.find("111213") != 0:
        points = points + 3
    return points

def pairs(hand, points):
    if hand.count(hand[0]) == 2:
        points = points + 1
    if hand.count(hand[2]) == 2:
        points = points + 1
    if hand.count(hand[4]) == 2:
        points = points + 1
    if hand.count(hand[6]) == 2:
        points = points + 1
    if hand.count(hand[8]) == 2:
        points = points + 1

    if hand.count(hand[0]) == 3:
        points = points + 2
    if hand.count(hand[2]) == 3:
        points = points + 2
    if hand.count(hand[4]) == 3:
        points = points + 2
    if hand.count(hand[6]) == 3:
        points = points + 2
    if hand.count(hand[8]) == 3:
        points = points + 2

    if hand.count(hand[0]) == 4:
        points = points + 3
    if hand.count(hand[2]) == 4:
        points = points + 3
    if hand.count(hand[4]) == 4:
        points = points + 3
    if hand.count(hand[6]) == 4:
        points = points + 3
    if hand.count(hand[8]) == 4:
        points = points + 3
    return points

def flush(hand, points):
    if hand[1] == hand[3] == hand[5] == hand[7]:
        points = points + 4
        if hand[1] == hand[9]:
            points = points + 1
    return points

def nobs(nextCheck,hand,points):
    for i in hand:
        if (nextCheck == True):
            nextCheck = False
            if (i == hand[9]):
                points = points +1
        if (i == "J"):
            nextCheck = True
    return points

points = nobs(nextCheck,hand,points) + flush(hand, points) + pairs(hand, points) + run(numList, points)
print(points)
