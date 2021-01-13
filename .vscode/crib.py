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

    if (numList[0] == "1" or numList[1] == "1" or numList[2] == "1" or numList[3] == "1" or numList[4] == "1") and (numList[0] == "2" or numList[1] == "2" or numList[2] == "2" or numList[3] == "2" or numList[4] == "2") and (numList[0] == "3" or numList[1] == "3" or numList[2] == "3" or numList[3] == "3" or numList[4] == "3"):
        if numList[0] == "4" or numList[1] == "4" or numList[2] == "4" or numList[3] == "4" or numList[4] == "4":
            if numList[0] == "5" or numList[1] == "5" or numList[2] == "5" or numList[3] == "5" or numList[4] == "5":
                points = points + 5
                print("run of 5")
            else:
                points = points + 4
                if numList.count("1") == 2 or numList.count("2") == 2 or numList.count("3") == 2 or numList.count("4") == 2:
                    points = points + 4
                    print("double run of 4")
                else:
                    print("run of 4")
        else:
            points = points + 3
            if numList.count("1") == 3 or numList.count("2") == 3 or numList.count("3") == 3:
                points = points + 6
                print("triple run of 3")
            elif (numList.count("1") == 2 and (numList.count("2") == 2 or numList.count("3") == 2)) or (numList.count("2") == 2 and numList.count("3") == 2):
                points = points + 9
                print("quadruple run of 3")
            else:
                print("run of 3")

    elif (numList[0] == "2" or numList[1] == "2" or numList[2] == "2" or numList[3] == "2" or numList[4] == "2") and (numList[0] == "3" or numList[1] == "3" or numList[2] == "3" or numList[3] == "3" or numList[4] == "3") and (numList[0] == "4" or numList[1] == "4" or numList[2] == "4" or numList[3] == "4" or numList[4] == "4"):
        if numList[0] == "5" or numList[1] == "5" or numList[2] == "5" or numList[3] == "5" or numList[4] == "5":
            if numList[0] == "6" or numList[1] == "6" or numList[2] == "6" or numList[3] == "6" or numList[4] == "6":
                points = points + 5
                print("run of 5")
            else:
                points = points + 4
                if numList.count("2") == 2 or numList.count("3") == 2 or numList.count("4") == 2 or numList.count("5") == 2:
                    points = points + 4
                    print("double run of 4")
                else:
                    print("run of 4")
        else:
            points = points + 3
            if numList.count("2") == 3 or numList.count("3") == 3 or numList.count("4") == 3:
                points = points + 6
                print("triple run of 3")
            elif (numList.count("2") == 2 and (numList.count("3") == 2 or numList.count("4") == 2)) or (numList.count("3") == 2 and numList.count("4") == 2):
                points = points + 9
                print("quadruple run of 3")
            else:
                print("run of 3")

    elif (numList[0] == "3" or numList[1] == "3" or numList[2] == "3" or numList[3] == "3" or numList[4] == "3") and (numList[0] == "4" or numList[1] == "4" or numList[2] == "4" or numList[3] == "4" or numList[4] == "4") and (numList[0] == "5" or numList[1] == "5" or numList[2] == "5" or numList[3] == "5" or numList[4] == "5"):
        if numList[0] == "6" or numList[1] == "6" or numList[2] == "6" or numList[3] == "6" or numList[4] == "6":
            if numList[0] == "7" or numList[1] == "7" or numList[2] == "7" or numList[3] == "7" or numList[4] == "7":
                points = points + 5
                print("run of 5")
            else:
                points = points + 4
                if numList.count("3") == 2 or numList.count("4") == 2 or numList.count("5") == 2 or numList.count("6") == 2:
                    points = points + 4
                    print("double run of 4")
                else:
                    print("run of 4")
        else:
            points = points + 3
            if numList.count("3") == 3 or numList.count("4") == 3 or numList.count("5") == 3:
                points = points + 6
                print("triple run of 3")
            elif (numList.count("3") == 2 and (numList.count("4") == 2 or numList.count("5") == 2)) or (numList.count("4") == 2 and numList.count("5") == 2):
                points = points + 9
                print("quadruple run of 3")
            else:
                print("run of 3")

    elif (numList[0] == "4" or numList[1] == "4" or numList[2] == "4" or numList[3] == "4" or numList[4] == "4") and (numList[0] == "5" or numList[1] == "5" or numList[2] == "5" or numList[3] == "5" or numList[4] == "5") and (numList[0] == "6" or numList[1] == "6" or numList[2] == "6" or numList[3] == "6" or numList[4] == "6"):
        if numList[0] == "7" or numList[1] == "7" or numList[2] == "7" or numList[3] == "7" or numList[4] == "7":
            if numList[0] == "8" or numList[1] == "8" or numList[2] == "8" or numList[3] == "8" or numList[4] == "8":
                points = points + 5
                print("run of 5")
            else:
                points = points + 4
                if numList.count("4") == 2 or numList.count("5") == 2 or numList.count("6") == 2 or numList.count("7") == 2:
                    points = points + 4
                    print("double run of 4")
                else:
                    print("run of 4")
        else:
            points = points + 3
            if numList.count("4") == 3 or numList.count("5") == 3 or numList.count("6") == 3:
                points = points + 6
                print("triple run of 3")
            elif (numList.count("4") == 2 and (numList.count("5") == 2 or numList.count("6") == 2)) or (numList.count("5") == 2 and numList.count("6") == 2):
                points = points + 9
                print("quadruple run of 3")
            else:
                print("run of 3")

    elif (numList[0] == "5" or numList[1] == "5" or numList[2] == "5" or numList[3] == "5" or numList[4] == "5") and (numList[0] == "6" or numList[1] == "6" or numList[2] == "6" or numList[3] == "6" or numList[4] == "6") and (numList[0] == "7" or numList[1] == "7" or numList[2] == "7" or numList[3] == "7" or numList[4] == "7"):
        if numList[0] == "8" or numList[1] == "8" or numList[2] == "8" or numList[3] == "8" or numList[4] == "8":
            if numList[0] == "9" or numList[1] == "9" or numList[2] == "9" or numList[3] == "9" or numList[4] == "9":
                points = points + 5
                print("run of 5")
            else:
                points = points + 4
                if numList.count("5") == 2 or numList.count("6") == 2 or numList.count("7") == 2 or numList.count("8") == 2:
                    points = points + 4
                    print("double run of 4")
                else:
                    print("run of 4")
        else:
            points = points + 3
            if numList.count("5") == 3 or numList.count("6") == 3 or numList.count("7") == 3:
                points = points + 6
                print("triple run of 3")
            elif (numList.count("5") == 2 and (numList.count("6") == 2 or numList.count("7") == 2)) or (numList.count("6") == 2 and numList.count("7") == 2):
                points = points + 9
                print("quadruple run of 3")
            else:
                print("run of 3")



    elif (numList[0] == "6" or numList[1] == "6" or numList[2] == "6" or numList[3] == "6" or numList[4] == "6") and (numList[0] == "7" or numList[1] == "7" or numList[2] == "7" or numList[3] == "7" or numList[4] == "7") and (numList[0] == "8" or numList[1] == "8" or numList[2] == "8" or numList[3] == "8" or numList[4] == "8"):
        if numList[0] == "9" or numList[1] == "9" or numList[2] == "9" or numList[3] == "9" or numList[4] == "9":
            if numList[0] == "10" or numList[1] == "10" or numList[2] == "10" or numList[3] == "10" or numList[4] == "10":
                points = points + 5
                print("run of 5")
            else:
                points = points + 4
                if numList.count("6") == 2 or numList.count("7") == 2 or numList.count("8") == 2 or numList.count("9") == 2:
                    points = points + 4
                    print("double run of 4")
                else:
                    print("run of 4")
        else:
            points = points + 3
            if numList.count("6") == 3 or numList.count("7") == 3 or numList.count("8") == 3:
                points = points + 6
                print("triple run of 3")
            elif (numList.count("6") == 2 and (numList.count("7") == 2 or numList.count("8") == 2)) or (numList.count("7") == 2 and numList.count("8") == 2):
                points = points + 9
                print("quadruple run of 3")
            else:
                print("run of 3")

    elif (numList[0] == "7" or numList[1] == "7" or numList[2] == "7" or numList[3] == "7" or numList[4] == "7") and (numList[0] == "8" or numList[1] == "8" or numList[2] == "8" or numList[3] == "8" or numList[4] == "8") and (numList[0] == "9" or numList[1] == "9" or numList[2] == "9" or numList[3] == "9" or numList[4] == "9"):
        if numList[0] == "10" or numList[1] == "10" or numList[2] == "10" or numList[3] == "10" or numList[4] == "10":
            if numList[0] == "11" or numList[1] == "11" or numList[2] == "11" or numList[3] == "11" or numList[4] == "11":
                points = points + 5
                print("run of 5")
            else:
                points = points + 4
                if numList.count("7") == 2 or numList.count("8") == 2 or numList.count("9") == 2 or numList.count("10") == 2:
                    points = points + 4
                    print("double run of 4")
                else:
                    print("run of 4")
        else:
            points = points + 3
            if numList.count("7") == 3 or numList.count("8") == 3 or numList.count("9") == 3:
                points = points + 6
                print("triple run of 3")
            elif (numList.count("7") == 2 and (numList.count("8") == 2 or numList.count("9") == 2)) or (numList.count("8") == 2 and numList.count("9") == 2):
                points = points + 9
                print("quadruple run of 3")
            else:
                print("run of 3")

    elif (numList[0] == "8" or numList[1] == "8" or numList[2] == "8" or numList[3] == "8" or numList[4] == "8") and (numList[0] == "9" or numList[1] == "9" or numList[2] == "9" or numList[3] == "9" or numList[4] == "9") and (numList[0] == "10" or numList[1] == "10" or numList[2] == "10" or numList[3] == "10" or numList[4] == "10"):
        if numList[0] == "11" or numList[1] == "11" or numList[2] == "11" or numList[3] == "11" or numList[4] == "11":
            if numList[0] == "12" or numList[1] == "12" or numList[2] == "12" or numList[3] == "12" or numList[4] == "12":
                points = points + 5
                print("run of 5")
            else:
                points = points + 4
                if numList.count("8") == 2 or numList.count("9") == 2 or numList.count("10") == 2 or numList.count("11") == 2:
                    points = points + 4
                    print("double run of 4")
                else:
                    print("run of 4")
        else:
            points = points + 3
            if numList.count("8") == 3 or numList.count("9") == 3 or numList.count("10") == 3:
                points = points + 6
                print("triple run of 3")
            elif (numList.count("8") == 2 and (numList.count("9") == 2 or numList.count("10") == 2)) or (numList.count("9") == 2 and numList.count("10") == 2):
                points = points + 9
                print("quadruple run of 3")
            else:
                print("run of 3")

    elif (numList[0] == "9" or numList[1] == "9" or numList[2] == "9" or numList[3] == "9" or numList[4] == "9") and (numList[0] == "10" or numList[1] == "10" or numList[2] == "10" or numList[3] == "10" or numList[4] == "10") and (numList[0] == "11" or numList[1] == "11" or numList[2] == "11" or numList[3] == "11" or numList[4] == "11"):
        if numList[0] == "12" or numList[1] == "12" or numList[2] == "12" or numList[3] == "12" or numList[4] == "12":
            if numList[0] == "13" or numList[1] == "13" or numList[2] == "13" or numList[3] == "13" or numList[4] == "13":
                points = points + 5
                print("run of 5")
            else:
                points = points + 4
                if numList.count("9") == 2 or numList.count("10") == 2 or numList.count("11") == 2 or numList.count("12") == 2:
                    points = points + 4
                    print("double run of 4")
                else:
                    print("run of 4")
        else:
            points = points + 3
            if numList.count("9") == 3 or numList.count("10") == 3 or numList.count("11") == 3:
                points = points + 6
                print("triple run of 3")
            elif (numList.count("9") == 2 and (numList.count("10") == 2 or numList.count("11") == 2)) or (numList.count("10") == 2 and numList.count("11") == 2):
                points = points + 9
                print("quadruple run of 3")
            else:
                print("run of 3")

    elif (numList[0] == "10" or numList[1] == "10" or numList[2] == "10" or numList[3] == "10" or numList[4] == "10") and (numList[0] == "11" or numList[1] == "11" or numList[2] == "11" or numList[3] == "11" or numList[4] == "11") and (numList[0] == "12" or numList[1] == "12" or numList[2] == "12" or numList[3] == "12" or numList[4] == "12"):
        if numList[0] == "13" or numList[1] == "13" or numList[2] == "13" or numList[3] == "13" or numList[4] == "13":
                points = points + 4
                if numList.count("10") == 2 or numList.count("11") == 2 or numList.count("12") == 2 or numList.count("13") == 2:
                    points = points + 4
                    print("double run of 4")
                else:
                    print("run of 4")
        else:
            points = points + 3
            if numList.count("10") == 3 or numList.count("11") == 3 or numList.count("12") == 3:
                points = points + 6
                print("triple run of 3")
            elif (numList.count("10") == 2 and (numList.count("11") == 2 or numList.count("12") == 2)) or (numList.count("11") == 2 and numList.count("12") == 2):
                points = points + 9
                print("quadruple run of 3")
            else:
                print("run of 3")

    elif (numList[0] == "11" or numList[1] == "11" or numList[2] == "11" or numList[3] == "11" or numList[4] == "11") and (numList[0] == "12" or numList[1] == "12" or numList[2] == "12" or numList[3] == "12" or numList[4] == "12") and (numList[0] == "13" or numList[1] == "13" or numList[2] == "13" or numList[3] == "13" or numList[4] == "13"):
            points = points + 3
            if numList.count("11") == 3 or numList.count("12") == 3 or numList.count("13") == 3:
                points = points + 6
                print("triple run of 3")
            elif (numList.count("11") == 2 and (numList.count("12") == 2 or numList.count("13") == 2)) or (numList.count("12") == 2 and numList.count("13") == 2):
                points = points + 9
                print("quadruple run of 3")
            else:
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