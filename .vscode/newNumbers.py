inputNumber = input("input a number ")
numberList = (list(inputNumber))
endNumber = ""
counter = 0
while counter < len(numberList):
    numberList[counter] = int(numberList[counter])
    counter = counter + 1
print (numberList)
counter = 0
while counter < len(numberList):
    numberList[counter] = (numberList[counter] + 1)
    numberList[counter] = str(numberList[counter])
    counter = counter + 1
    print (numberList)
counter = 0
while counter < len(numberList):
    endNumber = endNumber + numberList[counter]
    counter = counter + 1
print (endNumber)



