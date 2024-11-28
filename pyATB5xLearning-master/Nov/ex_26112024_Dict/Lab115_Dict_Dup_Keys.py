#p =  {"name" : "Pramod", "name": "Amit"}
#print(p)

mylist = [1, 2, 2, 3, 4, 4, 5]
#unique_value = set()
#result = {}
#mylist=list(dict.fromkeys(mylist))
#print(mylist)
for i in mylist:
    if i in mylist[mylist.index(i)+1:]:
       mylist.remove(i)
print(mylist)