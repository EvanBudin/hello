fAge = input("What is the father's age? ")
sAge = input("What is the son's age? ")
sAge = int(sAge)
fAge = int(fAge)
while (sAge != fAge/2):
    sAge = sAge + 1
    fAge = fAge + 1
print("The son is %s" % (sAge))
print("The father is %s" % (fAge))