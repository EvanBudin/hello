baseNumber = input("Enter Number ")
numberList = (list(baseNumber))
numberOfRuns = 0
while len(numberList) > 1:
    counter = 0
    while counter < len(numberList):
        numberList[counter] = int(numberList[counter])
        counter = counter + 1
    numberList = sum(numberList)
    numberList = str(numberList)
    numberList = (list(numberList))
    numberOfRuns = numberOfRuns + 1
print(numberOfRuns)
