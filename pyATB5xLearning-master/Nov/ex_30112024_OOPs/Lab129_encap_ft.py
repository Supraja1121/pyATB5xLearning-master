#web automation
#in real time we are going to automate pages
from dotenv import load_dotenv
import os

class VWLoginPage:
    def __init__(self,email_arg,password_arg):
        self.email = email_arg
        self.password = password_arg

    def login_confirm(self):
        if self.email == "dsf.df@sd.com" and self.password == "Pass123":
            print("Allowed, login success")

        else:
            print("login failed")

load_dotenv()
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

print(email, password)

vwo_obj = VWLoginPage(email, password)
vwo_obj.login_confirm()