class Person:
    name = None
    phone = None

    def __init__(self):
        print("I will be automatically called")
        self.name = input("enter the name\n")
        self.phone = input("enter the phone number\n")
    def details(self):
     print(f" name is {self.name}\n",f"phone is {self.phone}")

Anu = Person()
Anu.details()

bhanu = Person()
bhanu.details()
