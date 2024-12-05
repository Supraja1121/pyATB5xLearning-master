#Method overloading

class MathUnits:
    def add(self,a=1,b=20):
        print(a+b)

    def add(self,a=100,b=30,c=334):
        print(a+b+c)

d=MathUnits()
d.add(1,2,4)