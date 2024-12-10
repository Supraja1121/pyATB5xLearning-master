#static methods > a static method is a method that belongs to a class rather than an instance of a class.



class O:
    @staticmethod
    def sum(a,b):
        return a+b

    def sub(self,a,b):
        return a-b


o=O()
result = o.sub(3,2)
print(result)

print(O.sum(2,6))