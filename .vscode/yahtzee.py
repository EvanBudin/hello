intake = input("Enter a series of dice rolls: ")
intake = intake.split(", ")
print(intake)
intake = [int(x) for x in intake]
intake = [x * intake.count(x) for x in intake]
intake.sort(reverse = True)
print(intake[0])