class Parent:

    def home(self):
        print("2BHK")

class Son(Parent):

    def town(self):
        print("town")
    def home(self):
        print("3BHK")

o=Parent()
s=Son()
s.home()