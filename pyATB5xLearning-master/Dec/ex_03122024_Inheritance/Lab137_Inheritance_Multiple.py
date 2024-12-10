class A:
    def method(self):
        return "Method A"

class B:
    def method(self):
        return "Method B"

class C(B,A):
    def method(self):
     return "Method C"

c=C()
print(c.method())