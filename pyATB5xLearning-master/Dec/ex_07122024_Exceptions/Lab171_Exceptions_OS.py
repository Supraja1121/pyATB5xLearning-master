import os
from re import fullmatch
try:
    full_path = os.getcwd()
    print(full_path)
    full_path_file = full_path+ "/example.txt"
    print(full_path_file)

#read a file

    file = open(full_path_file)
except Exception as fnfe:
    print("file not found, fix the path or create a file")
finally:
    print("This code will be executed anyway")