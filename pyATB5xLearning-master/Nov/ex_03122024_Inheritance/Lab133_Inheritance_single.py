class Father:
    key="2bhk"

    def car(self):
        print("Father has a car -> Alto")
        print(self.key)


class Son(Father):
    key2 = "3bhk"


    def suv(Self):
        print("Son has a car -> Alto")
        print(Self.key)

obj=Father()
obj.car()

obj2=Son()
obj2.suv()

obj2.key= 123
print(obj2.key)