intake = input("Enter a series of dice rolls: ")
intake = intake.split()
intake = [int(i) for i in intake]
intake.sort()
counter = 0
for i in intake:
    intake[counter] = intake[counter] * (counter+1)
    counter = counter +1
print(intake)
