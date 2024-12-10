#Method overloading is not supported in python
class Calc:
    def sum(self,*args):
        for a in args:
            print(a)

c=Calc()
c.sum(2,3)