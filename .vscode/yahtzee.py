intake = input("Enter a series of dice rolls: ")
intake = intake.split(", ")
intake = [int(i) for i in intake]
intake.append(0)
intake[0],intake[1],intake[2],intake[3],intake[4],intake[5] = 6*intake.count(6),5*intake.count(5),4*intake.count(4),3*intake.count(3),2*intake.count(2),1*intake.count(1)
intake.sort(reverse = True)
print(intake[0])