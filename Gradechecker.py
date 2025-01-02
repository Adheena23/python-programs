# write a program to determine the grade based on marks
# criteris:
# marks >= 90: A
# marks >= 75: B
# marks >= 50: C
# else :f


marks = int(input("enter the marks: "))
if marks >= 90:
    print("Grade: A")
elif marks >= 75:
     print("Grade: B")
elif marks >= 50:
     print("Grade: C")
else:
    print("Grade: F")