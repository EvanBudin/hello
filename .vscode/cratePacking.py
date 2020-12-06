intake = input("Enter X, Y, x, y ")
intake.replace(" ", "", 3)
intake = intake.split(",")
intake = [int(value) for value in intake]
xValue = intake[0]/intake[2] - intake[0]%intake[2]/intake[2]
yValue = intake[1]/intake[3] - intake[1]%intake[3]/intake[3]
xRotate = intake[0]/intake[3] - intake[0]%intake[3]/intake[3]
yRotate = intake[1]/intake[2] - intake[1]%intake[2]/intake[2]
multiplied = (xValue*yValue)
rotated = (xRotate*yRotate)
if rotated >= multiplied:
    print(rotated)
else:
    print(multiplied)