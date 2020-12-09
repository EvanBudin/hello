# https://www.reddit.com/r/dailyprogrammer/comments/aphavc/20190211_challenge_375_easy_print_a_new_number_by/ for the challenge
def counterReset():
    counter = 0
inputNumber = input("input a number ")
numberList = (list(inputNumber))
endNumber = ""
counterReset()
while counter < len(numberList):
    numberList[counter] = int(numberList[counter])
    counter = counter + 1
print (numberList)
counterReset()
while counter < len(numberList):
    numberList[counter] = (numberList[counter] + 1)
    numberList[counter] = str(numberList[counter])
    counter = counter + 1
    print (numberList)
counterReset()
while counter < len(numberList):
    endNumber = endNumber + numberList[counter]
    counter = counter + 1
print (endNumber)
