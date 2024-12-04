class GrandFather:
    btc = "1"
    house = "three"

    def BHK(self):
        print("BHK")


class Parent(GrandFather):
    gold = "2kg"
    house = "5"

    def BHK2(self):
        print("2BHK")

class Child(Parent):
    diamond = "Diamond"

    def BHK3(self):
        print("3BHK")


cobj=Child()
print(cobj.house)
cobj.BHK2()
pobj=Parent()
pobj.BHK()
print(pobj.btc)
gfobj=GrandFather()
gfobj.BHK()
print(gfobj.house)