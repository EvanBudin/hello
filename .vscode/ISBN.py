def isbnMultiply():
    originalList[0] = originalList[0] * 10
    originalList[1] = originalList[1] * 9
    originalList[2] = originalList[2] * 8
    originalList[3] = originalList[3] * 7
    originalList[4] = originalList[4] * 6
    originalList[5] = originalList[5] * 5
    originalList[6] = originalList[6] * 4
    originalList[7] = originalList[7] * 3
    originalList[8] = originalList[8] * 2
    
originalNumber = input("Enter ISBN ")
originalList = list(originalNumber)
intList = []
counter = 0
if originalList[9] == 'X':
    originalList[9] = '10'
if len(originalList) == 10:
    while counter < len(originalList):
        originalList[counter] = int(originalList[counter])
        counter = counter + 1
    isbnMultiply()
    answer = sum(originalList)
    if answer % 11 == 0:
        print(True)
    else:
        print(False)
else:
    print(False)
