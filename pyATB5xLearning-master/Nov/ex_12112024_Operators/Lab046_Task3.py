#Problem to find the max between three numbers

#logic building
# user inputs int
#output int

#logic : if there is 1 condition we use "if else"
# If there are more conditions we use if elif else


a=int(input("num1\n"))
b=int(input("num2\n"))
c=int(input("num3\n"))

if a>b and a>c:
    print("max", a)
elif b>a and b>c:
    print("max", b)
else:print("max",c)

d=max(a,b,c)
print("max is",d)