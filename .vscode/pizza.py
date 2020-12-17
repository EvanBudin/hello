import math
diameter = input("What is the diameter of the pizza in inches? ")
price = input("What is the price of the pizza in dollars? ")
price = float(price)
diameter = int(diameter)
radius = diameter/2
radiusSquared = radius ** 2
area = radiusSquared * math.pi
pricePerInch = price / area
pricePerInch = round(pricePerInch, 2)
print("The price per square inch is %s" % (pricePerInch))