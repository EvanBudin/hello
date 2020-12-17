import math
speedLimit = input("What is the speed limit in mph? ")
avgSpeed = input("What is your average speed? ")
distance = input("What distance did you travel? ")
speedLimit = float(speedLimit)
avgSpeed = float(avgSpeed)
distance = float(distance)
speedLimit = speedLimit/60
avgSpeed = avgSpeed/60
answerLimit = distance/speedLimit
fastLimit = distance/avgSpeed
print("You saved %s minutes" % (round(answerLimit-fastLimit, 1)))