#Method overloading is not supported in python
class Calc:
    def sum(self,a,b):
        print(a+b)
    def sum(self,a,b,c):
        print(a+b+c)

c=Calc()
c.sum(2,4,1)