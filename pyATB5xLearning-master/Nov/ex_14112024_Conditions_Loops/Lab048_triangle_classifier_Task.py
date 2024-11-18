'''
Write a program that classifies a triangle based on its side lengths. Given three input values representing the lengths of the sides, determine if the triangle is equilateral (all sides are equal), isosceles (exactly two sides are equal), or scalene (no sides are equal). Use an if-else statement to classify the triangle.

equilateral : all sides equal

Isosceles : 2 sides are equal

Scalene : all are diff
'''

s1=int(input("enter side\n"))
s2=int(input("enter side\n"))
s3=int(input("enter side\n"))

if (s1==s2 and s1==s3):
    print("it is a equilateral triangle")
elif (s1==s2 or s1==s3 or s2==s3):
    print("it's a isosceles triangle")
else:
    print("it's a scalene triangle")
