class Father:
    def father(self):
        return 5
    def home(self):
        return "Father's home"
class Mother:
    def mother(self):
        print("2")
    def home(self):
        return "Mother's home"
#class Son(Father,Mother):
class Son(Mother,Father):
    def print_info(self):
        print("son..")

fobj=Father()
mobj=Mother()
sobj=Son()

sobj.mother()