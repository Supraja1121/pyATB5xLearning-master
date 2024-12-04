class PyATB:
  # attributes > what you have
    name = None
    email = None
    address = None
    phone = None
    company = None

#behaviour > what you can do
    def __init__(self,name,email,address,phone,company):  #no return no argument
     print("PC")
     self.name = name
     self.email = email
     self.address = address
     self.phone = phone
     self.company = company

    def talk(self):
     print(self.name+ " is talking")

    def work(self):
     print(self.name+ " is working")

    def walk(self):
     print(self.name+ " is walking")


#object Ref
indu_ref = PyATB("indu", "sd.dsfg@dfg.vom","address of indu", 456789,"cds")
print(f" name is : {indu_ref.name}\n",f"email is : {indu_ref.email}\n",f"address is : {indu_ref.address}\n",f"phone is : {indu_ref.phone}\n",f"company is : {indu_ref.company}\n")
indu_ref.talk()
indu_ref.work()
indu_ref.walk()

bindu_ref = PyATB("bindu", "sd.dsfg@dfg.vom","address of bindu", 1456789,"cds")
print(bindu_ref.name,bindu_ref.email,bindu_ref.address,bindu_ref.phone,bindu_ref.company)
bindu_ref.talk()
bindu_ref.work()
bindu_ref.walk()

sindu_ref = PyATB("sindhu", "sd.dsfg@dfg.vom","address of bindu", 1456789,"cds")
print(sindu_ref.name,sindu_ref.email,sindu_ref.address,sindu_ref.phone,sindu_ref.company)
sindu_ref.talk()
sindu_ref.work()
sindu_ref.walk()