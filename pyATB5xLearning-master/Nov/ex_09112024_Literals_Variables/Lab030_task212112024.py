#Task 2
#take 2 inputs from user
#print the quotient and reminder

a=int(input("enter num1"))
b=int(input("enter num2"))
q=a//b
r=a%b
print(f"Quotient(Q) -> {q}")
print(f"Remainder(R) -> {r}")

x,y=divmod(int(input("num1")),int(input("num2")))
print(x,y)