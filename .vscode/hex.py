intake = input("Enter 3 numbers ")
intake = intake.split(", ")
intake = [int(x) for x in intake]
intake = [hex(x) for x in intake]
intake = [str(x) for x in intake]
intake = [x.replace("0x", "") for x in intake]
print(intake[0]+intake[1]+intake[2])