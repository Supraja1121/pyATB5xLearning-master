'''Create a program that determines whether a given year is a leap year. A leap year is divisible by 4, but not by 100 unless it is also divisible by 400. Use an if-else statement to make this determination.
leap is divisible by 4 -> reminder when divided by 4 is 0
not divisible by 100
divisible by 400


leap day occurs in each year
that is a multiple of 4,
except for years
evenly divisible by 100
but not by 400.
'''

year=int(input("enter year\n"))

if ((year%4 == 0) and (year % 100 != 0) or (year%400 == 0)):
    print("It is a leap year")
else:
    print("It is not a leap year")