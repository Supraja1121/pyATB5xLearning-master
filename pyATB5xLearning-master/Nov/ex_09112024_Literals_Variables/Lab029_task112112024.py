#Task
#take 3 inputs from user
#perform sum, sub, mul and div

#logic building
#1 - i/p and o/p
a=float(input("enter a"))
b=float(input("enter b"))
c=float(input("enter c"))

sum = a+b+c
sub = a-b-c
mul = a*b*c
div = (a/b)/c

'''print(a+b+c)
print(a-b-c)
print(a*b*c)
print(a/b/c)'''

print((a+b+c),"sum",'\n',(a-b-c),"sub",'\n',(a*b*c),"mul",'\n',(a/b/c),"div")