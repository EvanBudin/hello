var1 = input("Enter first number ")
operator = input("Enter operator ")
var2 = input("Enter second number ")
var1 = float(var1)
var2 = float(var2)
if operator == "+":
    print(var1 + var2)
elif operator == "*":
    print(var1 * var2)
elif operator == "/":
    print(var1 / var2)
elif operator == "-":
    print(var1 - var2)
else:
    print("invalid operator")