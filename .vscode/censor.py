intake = input("Enter sentance and vowels: ")
intake = intake.split(",")
second = intake[1]
intake.pop(1)
second = list(second)
intake = intake[0]+""
print(second)
print(intake)
while intake.find("*") != -1:
    num = second[0]
    intake = intake.replace("*",num, 1)
    second.pop(0)
print(intake)