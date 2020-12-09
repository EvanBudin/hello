isSolved = 0
intake = input("How many people does each person know? ")
intake = intake.split(" ")
intake = [int(x) for x in intake]

while isSolved == 0:
    while intake.count(0) != 0:
        intake.remove(0)
    if len(intake) == 0:
        isSolved = 1
        break
    intake.sort(reverse = True)
    N = intake[0]
    intake.remove(N)
    if N > len(intake):
        isSolved = -1
        break
    counter = 0
    for x in range(N):
        intake[counter] = intake[counter]-1
        counter = counter+1
if isSolved == 1:
    print(True)
elif isSolved == -1:
    print(False)