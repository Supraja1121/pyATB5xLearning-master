#Custom exception
class LowBalExcCustom(Exception):
    def __init__(self,message):
        self.message  = message
        super().__init__(message)


balance = 100
withdraw = int(input("enter the amount you want to withdraw"))
if withdraw > balance:
    raise LowBalExcCustom("Balance is low")
else:
    print("Remaining balance", (balance-withdraw))
