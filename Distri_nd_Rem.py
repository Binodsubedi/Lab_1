import math

num1 = int(input("Enter the numbers of apples:"))
num2 = int(input("Enter the numbers of people:"))
Remaining = num1%num2
per_person = math.floor(num1/num2)
print("Number of apples per person is=",per_person)
print("Number of apples remaining in the basket is=", Remaining)