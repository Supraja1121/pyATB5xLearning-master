'''
write a program that calculates and displays the letter grade for a given numerical score(eg., A,B,C,D,F) based on the following grading scale.

A: 90-100
B: 80-89
C: 70-79
D= 60-69
F= 0-59


percentage=int(input("Enter percentage\n"))

if percentage in range(90,100):
    print("Grade A")
elif percentage in range(80, 89):
    print("Grade A")
elif percentage in range(70, 79):
    print("Grade A")
elif percentage in range(60, 69):
    print("Grade A")
else:
    print("Fail")
'''

percentage=int(input("Enter percentage\n"))

if percentage >=90 and percentage <=100:
    print("Grade A")
elif percentage >=80 and percentage <=89:
    print("Grade B")
elif percentage >=70 and percentage <=79:
    print("Grade C")
elif percentage >=60 and percentage <=69:
    print("Grade D")
elif percentage >100:
    print("no grade")
elif percentage <0:
    print("less than 0")
else:
    print("Fail")