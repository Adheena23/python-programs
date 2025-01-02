# Write a program to check whether an input character is uppercase, lowercase, or not an alphabet

char = input("Enter a single character: ")

if 'A' <= char <= 'Z':
    print("Uppercase letter")
elif 'a' <= char <= 'z':
    print("Lowercase letter")
else:
    print("Not an alphabet")
