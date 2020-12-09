# https://www.reddit.com/r/dailyprogrammer/comments/ffxabb/20200309_challenge_383_easy_necklace_matching/ for the challenge
# The next 2 lines get the input and set them equal to the variable
originalNecklace = input("Enter original necklace ")
newNecklace = input("Enter new necklace ")
# doubles the original word, for example nicole becomes nicolenicole
twoNecklace = originalNecklace * 2
#says that its not the same necklace if they have a different number of characters
if len(originalNecklace) != len(newNecklace):
    print(False)
#it tries to find the new necklaces name in the doubled one, for example finding icolen in nicolenicole
elif twoNecklace.find(newNecklace) != -1:
    print(True)
#if it can't find it, it is not the same necklace
else:
    print(False)

runCounter = 0
originalNecklace = list(originalNecklace)
if len(originalNecklace) ==0:
    originalNecklace.append("")
rotateNecklace = []
rotateNecklace = list(originalNecklace)
for x in range(len(rotateNecklace)):
    rotateNecklace.append(rotateNecklace[0])
    rotateNecklace.pop(0)
    print(originalNecklace)
    print(rotateNecklace)
    if rotateNecklace == originalNecklace:
        runCounter = runCounter + 1

print(runCounter)