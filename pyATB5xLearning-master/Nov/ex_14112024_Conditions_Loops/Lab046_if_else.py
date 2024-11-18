#find max between 3

'''syntax
if condition 1:
print("do 1")
if condition 2:
print("do 2")
if condition 3:
print("do 3")
else:
print("do 4")
'''
a=int(input("enter num1\n"))
b=int(input("enter num2\n"))
c=int(input("enter num3\n"))

if a>b and a>c:
    print("max is", a)
elif b>a and b>c:
    print("max is", b)
else:
    print("max is", c)