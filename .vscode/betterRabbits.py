# moves every age group one to the right in the female list
def ageFemale():
    counter = 95
    for z in reversed(femaleRabbits):
        femaleRabbits[counter] = femaleRabbits[counter - 1]
        counter = counter - 1
# moves every age group one to the right in the male list
def ageMale():
    counter = 95
    for z in reversed(maleRabbits):
        maleRabbits[counter] = maleRabbits[counter - 1]
        counter = counter -1
# sets values
init = input("Enter Rabbit Values: ")
init = init.split(" ")
init = [int(y) for y in init]
femaleRabbits = []
maleRabbits = []
dead = 0
maleBabyHolder = 0
runCounter=0
femaleBabyHolder = 0
# makes the lists the length of a rabbits life and inputs original rabbits
for x in range(96):
    femaleRabbits.append(0)
    maleRabbits.append(0)
maleRabbits[2] = init[0]
femaleRabbits[2] = init[1]
totalRabbitsNeeded = init[2]
totalRabbits = sum(femaleRabbits) + sum(maleRabbits)
# does the aging then adds the babies
while totalRabbits < totalRabbitsNeeded:
    fertileRabbits = sum(femaleRabbits)- femaleRabbits[0]-femaleRabbits[1]-femaleRabbits[2]-femaleRabbits[3]
    maleBabyHolder = fertileRabbits*5
    femaleBabyHolder = fertileRabbits*9
    ageFemale()
    dead = dead + femaleRabbits[0]
    femaleRabbits[0] = femaleBabyHolder
    ageMale()
    dead = dead + maleRabbits[0]
    maleRabbits[0] = maleBabyHolder
    runCounter = runCounter+1
    totalRabbits = sum(maleRabbits) + sum(femaleRabbits)
print(runCounter)
print(dead)

