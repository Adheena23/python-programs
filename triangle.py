#  Check Triangle Validity
# Write a program to check whether three given sides can form a valid triangle. A triangle is valid if the sum of any two sides is greater than the third side

a = int(input("Enter side 1: "))
b = int(input("Enter side 2: "))
c = int(input("Enter side 3: "))

if a + b > c and a + c > b and b + c > a:
    print("The sides form a valid triangle.")
else:
    print("The sides do not form a valid triangle.")
