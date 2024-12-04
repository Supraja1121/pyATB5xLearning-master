class Person:
  # attributes > what you have
    name = None
    email = None
    address = None

#behaviour > what you can do
    def __init__(self,name,email):  #no return no argument
     print("PC")
     self.name = name
     self.email = email

    def talk(self):
     print(self.name+ " is talking")

    def sleep(self):
     pass

#object Ref
indu_ref = Person("indu", "sd.dsfg@dfg.vom")
print(indu_ref.name)
print(indu_ref.email)
indu_ref.talk()


bindu_ref = Person("bindu","sfd.f@df.cpm")
print(bindu_ref.name)
print(bindu_ref.email)
bindu_ref.talk()

sindhu_ref= Person("sindhu","email of Sindhu")
print(sindhu_ref.name,",",sindhu_ref.email)