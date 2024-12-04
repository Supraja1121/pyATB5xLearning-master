class Person:
    def __init__(self,name):
        self.name=name

    def walk(self):
        return self.name

amit = Person("amit")
pramod = Person("pramod")

print(amit.name)
print(pramod.name)

print(amit.walk() + " is walking")
print(pramod.walk() + " is walking")

