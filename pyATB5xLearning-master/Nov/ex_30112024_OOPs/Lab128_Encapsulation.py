#web automation
#in real time we are going to automate pages

class VWLoginPage:
    def __init__(self,email_arg,password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "dsf.df@sd.com" and self.password == "Pass123":
            print("Allowed, login success")

        else:
            print("login failed")

email = input("Enter email \n")
password = input("enter password\n")


vwo_obj = VWLoginPage(email, password)
vwo_obj.login_confirm()

#test = VWLoginPage("dsf.df@sd.com","Pass123")
#test.login_confirm()