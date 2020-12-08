init = input("Enter Rabbit Values: ")
init = init.split(" ")
init = [int(x) for x in init]
femaleRabbits = []
maleRabbits = []
dead = 0
maleBabyHolder = 0
runCounter=0
femaleBabyHolder = 0
for x in range(96):
    femaleRabbits.append(0)
    maleRabbits.append(0)
maleRabbits[2] = init[0]
femaleRabbits[2] = init[1]
totalRabbitsNeeded = init[2]
totalRabbits = sum(femaleRabbits) + sum(maleRabbits)

while totalRabbits < totalRabbitsNeeded:
    counter = 96
    fertileRabbits = sum(femaleRabbits)- femaleRabbits[0]-femaleRabbits[1]-femaleRabbits[2]-femaleRabbits[3]
    maleBabyHolder = fertileRabbits*5
    femaleBabyHolder = fertileRabbits*9
    for z in reversed(femaleRabbits):
        femaleRabbits[counter - 1] = femaleRabbits[counter - 2]
        counter = counter - 1
    dead = dead + femaleRabbits[0]
    femaleRabbits[0] = femaleBabyHolder
    counter = 96
    for z in reversed(maleRabbits):
        maleRabbits[counter-1] = maleRabbits[counter - 2]
        counter = counter -1
    dead = dead + maleRabbits[0]
    maleRabbits[0] = maleBabyHolder
    runCounter = runCounter+1
    totalRabbits = sum(maleRabbits) + sum(femaleRabbits)
print(runCounter)
print(dead)