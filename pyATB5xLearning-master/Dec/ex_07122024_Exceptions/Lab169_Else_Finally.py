import os
#OS module is a powerful module in python that provides functions to interact with Operating System.

print(os.getcwd())
#Returns the current working directory

#list files in the directory
files=os.listdir('/Users/psupr/Downloads/pyATB5xLearning-master/pyATB5xLearning-master/')
print(f"Files in the current directory: {files}")

# Create a new Directory
os.mkdir('Test2')