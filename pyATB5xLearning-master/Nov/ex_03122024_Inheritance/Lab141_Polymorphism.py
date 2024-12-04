#Method overloading

class Dog:
    def bark(self):
        print("Dog is barking")

    def bark(self,breed):
        print(f"Dog with {breed} is barking")

d=Dog()
d.bark("chow")