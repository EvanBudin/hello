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
print(numList)


def fifteens(numList,points):
    counter = 0
    for i in numList:
        if i == (11):
            numList[counter] = 10
        counter = counter + 1
    counter = 0
    for i in numList:
        if i == (12):
            numList[counter] = 10
        counter = counter + 1
    counter = 0
    for i in numList:
        if i == (13):
            numList[counter] = 10
        counter = counter + 1
    print(numList)
    if numList[0] + numList[1] == 15:
        points = points + 2
        print("fifteen")
    if numList[0] + numList[2] == 15:
        points = points + 2
        print("fifteen")
    if numList[0] + numList[3] == 15:
        points = points + 2
        print("fifteen")
    if numList[0] + numList[4] == 15:
        points = points + 2
        print("fifteen")
    if numList[1] + numList[2] == 15:
        points = points + 2
        print("fifteen")
    if numList[1] + numList[3] == 15:
        points = points + 2
        print("fifteen")
    if numList[1] + numList[4] == 15:
        points = points + 2
        print("fifteen")
    if numList[2] + numList[3] == 15:
        points = points + 2
        print("fifteen")
    if numList[2] + numList[4] == 15:
        points = points + 2
        print("fifteen")
    if numList[3] + numList[4] == 15:
        points = points + 2
        print("fifteen")

    if numList[0] + numList[1] + numList[2] == 15:
        points = points + 2
        print("fifteen")
    if numList[0] + numList[1] + numList[3] == 15:
        points = points + 2
        print("fifteen")
    if numList[0] + numList[1] + numList[4] == 15:
        points = points + 2
        print("fifteen")
    if numList[0] + numList[2] + numList[3] == 15:
        points = points + 2
        print("fifteen")
    if numList[0] + numList[2] + numList[4] == 15:
        points = points + 2
        print("fifteen")
    if numList[0] + numList[3] + numList[4] == 15:
        points = points + 2
        print("fifteen")
    if numList[1] + numList[2] + numList[3] == 15:
        points = points + 2
        print("fifteen")
    if numList[1] + numList[2] + numList[4] == 15:
        points = points + 2
        print("fifteen")
    if numList[1] + numList[3] + numList[4] == 15:
        points = points + 2
        print("fifteen")
    if numList[2] + numList[3] + numList[4] == 15:
        points = points + 2
        print("fifteen")

    if numList[0] + numList[1] + numList[2] + numList[3] == 15:
        points = points + 2
        print("fifteen")
    if numList[0] + numList[1] + numList[2] + numList[4] == 15:
        points = points + 2
        print("fifteen")
    if numList[0] + numList[1] + numList[3] + numList[4] == 15:
        points = points + 2
        print("fifteen")
    if numList[0] + numList[2] + numList[3] + numList[4] == 15:
        points = points + 2
        print("fifteen")
    if numList[1] + numList[2] + numList[3] + numList[4] == 15:
        points = points + 2
        print("fifteen")

    if numList[0] + numList[1] + numList[2] + numList[3] + numList[4] == 15:
        points = points + 2
        print("fifteen")
    return points

# This function calculates points scored by runs by checking for every possible run in the game
def run(numList, points):
    numList = [str(i) for i in numList]
    numList = numList[0] + numList[1] + numList[2] + numList[3] + numList[4]
    if numList.find("123") != -1:
        if numList.find("1234") != -1:
            if numList.find("12345") != -1:
                points = points + 5
                print("run of 5")
            else:
                points = points + 4
                print("run of 4")
        else:
            points = points + 3
            print("run of 3")
    elif numList.find("234") != -1:
        if numList.find("2345") != -1:
            if numList.find("23456") != -1:
                points = points + 5
                print("run of 5")
            else:
                points = points + 4
                print("run of 4")
        else:
            points = points + 3
            print("run of 3")
    elif numList.find("345") != -1:
        if numList.find("3456") != -1:
            if numList.find("34567") != -1:
                points = points + 5
                print("run of 5")
            else:
                points = points + 4
                print("run of 4")
        else:
            points = points + 3
            print("run of 3")
    elif numList.find("456") != -1:
        if numList.find("4567") != -1:
            if numList.find("45678") != -1:
                points = points + 5
                print("run of 5")
            else:
                points = points + 4
                print("run of 4")
        else:
            points = points + 3
            print("run of 3")
    elif numList.find("567") != -1:
        if numList.find("5678") != -1:
            if numList.find("56789") != -1:
                points = points + 5
                print("run of 5")
            else:
                points = points + 4
                print("run of 4")
        else:
            points = points + 3
            print("run of 3")
    elif numList.find("678") != -1:
        if numList.find("6789") != -1:
            if numList.find("678910") != -1:
                points = points + 5
                print("run of 5")
            else:
                points = points + 4
                print("run of 4")
        else:
            points = points + 3
            print("run of 3")
    elif numList.find("789") != -1:
        if numList.find("78910") != -1:
            if numList.find("7891011") != -1:
                points = points + 5
                print("run of 5")
            else:
                points = points + 4
                print("run of 4")
        else:
            points = points + 3
            print("run of 3")
    elif numList.find("8910") != -1:
        if numList.find("891011") != -1:
            if numList.find("89101112") != -1:
                points = points + 5
                print("run of 5")
            else:
                points = points + 4
                print("run of 4")
        else:
            points = points + 3
            print("run of 3")
    elif numList.find("91011") != -1:
        if numList.find("9101112") != -1:
            if numList.find("910111213") != -1:
                points = points + 5
                print("run of 5")
            else:
                points = points + 4
                print("run of 4")
        else:
            points = points + 3
            print("run of 3")
    elif numList.find("101112") != -1:
        if numList.find("10111213") != -1:
            points = points + 4
            print("run of 4")
        else:
            points = points + 3
            print("run of 3")
    elif numList.find("111213") != -1:
        points = points + 3
        print("run of 3")
    return points
# This function checks for pairs by seeing if there is more than one of each card, and adds the amount of points divided by the number of cards needed per card
def pairs(hand, points):
    if hand.count(hand[0]) == 2:
        points = points + 1
        print("pair")
    if hand.count(hand[2]) == 2:
        points = points + 1
        print("pair")
    if hand.count(hand[4]) == 2:
        points = points + 1
        print("pair")
    if hand.count(hand[6]) == 2:
        points = points + 1
        print("pair")
    if hand.count(hand[8]) == 2:
        points = points + 1
        print("pair")

    if hand.count(hand[0]) == 3:
        points = points + 2
        print("three of a kind")
    if hand.count(hand[2]) == 3:
        points = points + 2
        print("three of a kind")
    if hand.count(hand[4]) == 3:
        points = points + 2
        print("three of a kind")
    if hand.count(hand[6]) == 3:
        points = points + 2
        print("three of a kind")
    if hand.count(hand[8]) == 3:
        points = points + 2
        print("three of a kind")

    if hand.count(hand[0]) == 4:
        points = points + 3
        print("four of a kind")
    if hand.count(hand[2]) == 4:
        points = points + 3
        print("four of a kind")
    if hand.count(hand[4]) == 4:
        points = points + 3
        print("four of a kind")
    if hand.count(hand[6]) == 4:
        points = points + 3
        print("four of a kind")
    if hand.count(hand[8]) == 4:
        points = points + 3
        print("four of a kind")
    return points
# This function checks for flushes
def flush(hand, points):
    if hand[1] == hand[3] == hand[5] == hand[7]:
        if hand[1] == hand[9]:
            points = points + 5
            print("flush of 5")
        else:
            points = points + 4
            print("flush of 4")
    return points
#This function checks for nobs on every Jack
def nobs(nextCheck,hand,points,counter):
    counter = 0
    for i in hand:
        if (nextCheck == True):
            nextCheck = False
            if (i == hand[9]):
                points = points +1
                print("nobs")
        if (i == "J") and counter != 8:
            nextCheck = True
        counter = counter + 1
    return points

points = nobs(nextCheck,hand,points,counter) + flush(hand, points) + pairs(hand, points) + run(numList, points) + fifteens(numList, points)
print(points)