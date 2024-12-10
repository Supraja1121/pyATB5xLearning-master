file_name = "ss.txt"
content="this is a ss's file"

with open(file_name, "w") as file:
    file.write(content)


with open(file_name, "r") as file:
    content2 = file.read()
    print(content2)

