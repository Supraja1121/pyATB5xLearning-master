#Abstractiom
#Hide details and show what is required
#Abstarction : Abstract base class

from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self,name):
        self.name = name
        print(self.name)

    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):

    def make_sound(self):
        print("Bark")

d=Dog("puppy")
d.make_sound()