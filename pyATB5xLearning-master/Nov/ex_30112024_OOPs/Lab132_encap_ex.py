class Home:

    def __init__(self):
        self.public_var = "father"
        self.__private_var = "child"

    def mom(self):
        print(self.__private_var)
        self.__wife()

    def __wife(self):
        print("pWife")
obj_ref = Home()
obj_ref.mom()
print(obj_ref.public_var)
