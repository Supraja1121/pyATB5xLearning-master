"""
write a program to take inputs from users and sum,mul,div the number
"""
from urllib.parse import uses_query

#logic building formula
# step1
# i/p ->int
# o/p -> sum-int sub - int mul int div- float


# step2  i/p
# step3  o/p

num1=int(input("enter int num1"))
num2=int(input("enter int num2"))

#or we can uses_query#num1 = int(num1)

print("sum is",(num1 + num2))
print("sub is",(num1 - num2))
print("mul is",(num1 * num2))
print("div is",(num1 / num2))