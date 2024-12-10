from abc import ABC, abstractmethod

class Father():
    def __init__(self,name):
        self.name = name
    @abstractmethod
    def loan(self):
        pass

class Son(Father):
    def loan(self):
        print("pays father's loan")

f=Father("devid")
f.loan()
s=Son("rahul")
s.loan()