# match statement works where python version is greater than 3.10

#syntax:

# match variable:
#   case pattern 1:
#      #code block
# case pattern 2:
# code block

# Write a program to ask user which browser he want to use to automate.
browser = input("enter name of the browser\n")
match browser:
    case "firefox":
        print("ff")
    case "chrome":
        print("c")
    case "edge":
        print("e")
    case "safari":
        print("e")
    case _: #default
        print("not valid browser")
