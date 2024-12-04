class Bank:

    def __init__(self,acc_no,bal):
        self.bal=bal#public
        self.__acc_no=acc_no#private

    def check_bal(self):
        print(self.bal)


    def deposit(self,amount):
        self.bal=self.bal+amount

    def show_me_acc_no(self,is_auth):
        if is_auth == True:
            print(self.__acc_no)
        else:
            print("not allowed")

    def __internal_private(self):
        print("private method can be accessed only by this class")

icici = Bank(98765,100)
icici.deposit(200)
icici.check_bal()
print(icici.bal)
icici.show_me_acc_no(True)