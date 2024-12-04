class Parent:
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