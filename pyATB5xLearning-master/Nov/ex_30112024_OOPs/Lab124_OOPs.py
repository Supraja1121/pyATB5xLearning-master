a=10

class Person:
    b=11 # instance variable


    def print_info(self):
        c=20 #local variable
        print(c)
        print(self.b)
        global a
        print(a)


object_ref = Person()
object_ref.print_info()