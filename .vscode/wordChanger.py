input1 = input("Enter First Word: ")
input2 = input("Enter Second Word: ")
counter = 0
print(input1)
print(input2)
if len(input1) == len(input2):
   while input1 != input2:
       input1 = list(input1)
       input2 = list(input2)
       input1[counter] = input2[counter]
       counter = counter + 1
       print(input1)
else:
    print("Words are different length")