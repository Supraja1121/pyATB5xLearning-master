class Father:
    def BHK1(self):
        print("F1BHK")

class Ani(Father):
    def BHK2(self):
        print("a2BHK")

class Supraja(Father):
    def BHK3(self):
        print("s3BHK")

class Lucky(Father):
    def BHK4(self):
        print("l4BHK")

f=Father()
f.BHK1()
a=Ani()
a.BHK2()
a.BHK1()
s=Supraja()
s.BHK1()
s.BHK3()
l=Lucky()
l.BHK1()
l.BHK4()