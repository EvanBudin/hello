initList = input("Enter List: ")
initList = initList.split(" ")
counter = 0
initList = [int(x) for x in initList]
femaleRabbitList= [0, 0, initList[1]]
maleRabbitList= [0, 0, initList[0]]
for x in range(3, 98):
    femaleRabbitList.append(0)
for x in range(3,98):
    maleRabbitList.append(0)
maleRabbitList.reverse()
femaleRabbitList.reverse()
rabbitSum = sum(femaleRabbitList) + sum(maleRabbitList)

while rabbitSum < initList[2]:
    for x in femaleRabbitList:
        x = femaleRabbitList[x+1]
    for x in maleRabbitList:
        x = maleRabbitList[x+1]
    fertileRabbitSum= sum(femaleRabbitList)
    femaleRabbitList[96] = fertileRabbitSum*9
    maleRabbitList[96] = fertileRabbitSum*5
    counter = counter+1
    rabbitSum = sum(femaleRabbitList) + sum(maleRabbitList)
print(counter)