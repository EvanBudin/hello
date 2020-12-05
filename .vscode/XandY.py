string = input("enter a series of x's and y's ")
numberX = 0
numberY = 0
while string.find("x") != -1:
    string = string.replace("x", "", 1)
    numberX = numberX + 1
while string.find("y") != -1:
    string = string.replace("y", "", 1)
    numberY = numberY + 1
if numberX == numberY:
    print(True)
else:
    print(False)
