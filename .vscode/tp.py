import math
people = input("How many people are in the household? ")
rolls = input("how many rolls of toilet paper do you have? ")
people = int(people)
rolls = int(rolls)
dailyUsed = people * 57
totalPieces = rolls * 500
print(math.floor(totalPieces/dailyUsed))