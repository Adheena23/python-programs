# Write a program to count the number of vowels in a given string using a for loop

string = input("Enter a string: ")
vowels = 'aeiouAEIOU'
count = 0
for char in string:
    if char in vowels:
        count += 1
print(f"Number of vowels in the string: {count} ")
