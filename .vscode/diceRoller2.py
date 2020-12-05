import random
dice = input("Enter number and type of dice. ")
dice = dice.split("d")
count1 = count2 = count3 = count4 = count5 = count6 = count7 = count8 = count9 = count10 = count11 = count12 = count13 = count14 = count15 = count16 = count17 = count18 = count19 = count20 = 0
counter = 0
dice[0] = int(dice[0])
dice[1] = int(dice[1])
list = []
while counter < dice[0]:
    list.append(random.randint(1,dice[1]))
    counter = counter + 1
answer = sum(list)
print(answer)