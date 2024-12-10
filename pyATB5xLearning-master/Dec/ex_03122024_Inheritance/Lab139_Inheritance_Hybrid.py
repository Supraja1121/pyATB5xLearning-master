class Father:
    def father(self):
        print("father")

class Supraja(Father):
    def supraja(self):
        print("supraja")


class Ani(Father):
    def ani(self):
        print("ani")


class Lucky(Supraja,Ani):
    def lucky(self):
        print("lucky")

l=Lucky()
l.father()
l.supraja()
l.ani()
l.lucky()




