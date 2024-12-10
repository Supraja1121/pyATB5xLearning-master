print("start of the program")
try:
  a= int(input("enter the num1"))
  b= int(input("enter the num2"))
  c=a/b
  print("result is ", c)
except Exception as e:
  print(e)
print("end of the program")
#try and except