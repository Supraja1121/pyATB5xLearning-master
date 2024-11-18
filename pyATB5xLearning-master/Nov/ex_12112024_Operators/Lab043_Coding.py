# Write a python program to calculate area of a circle
# Using formula area=Π*r^2
# pi=3.14

r = float(input("enter radius\n"))
#pi = 3.14
area= 3.14*(r**2)
#print(area)
#print(f"area of the circle is {area:.3f}")
#print("Area of the circle is ->", area)

# * > mul
# ** > pow

import math
print(math.pow(r,2))
area = math.pi * math.pow(r,2)
print("Area of the circle is", area)

#donot use one liners > print(3.14*(float(input("enter radius\n"))**2))

import math

print(math.pi)
print(math.pow(2,2))
print(math.sin(90))
print(math.cos(90))
print(math.tan(90))