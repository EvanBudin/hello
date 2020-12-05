import random
dice = input("Enter number and type of dice. ")
dice = dice.split("d")
counter = 0
dice[0] = int(dice[0])
dice[1] = int(dice[1])
list = []
while counter < dice[0]:
    list.append(random.randint(1,dice[1]))
    counter = counter + 1
answer = sum(list)
print(answer)
print(list)