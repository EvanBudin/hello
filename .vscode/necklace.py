# https://www.reddit.com/r/dailyprogrammer/comments/ffxabb/20200309_challenge_383_easy_necklace_matching/ for the challenge
originalNecklace = input("Enter original necklace ")
newNecklace = input("Enter new necklace ")
twoNecklace = originalNecklace * 2

if len(originalNecklace) != len(newNecklace):
    print(False)
elif twoNecklace.find(newNecklace) != -1:
    print(True)
else:
    print(False)