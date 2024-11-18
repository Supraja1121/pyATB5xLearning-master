#write a program to let the user know if he/she can attend the club
#age is 21

#logic building

# Step 1
# use input i/p -> data type -> int
#o/p > string > user can go

# Step 2 Rough logic
# age >21 -> can go
# age <21 -> cant go

# Step 3

age =int(input("enter your age:\n"))
#if age in range(21,130):
if age >=21 and age <=130:
    print("you can go to the Club")
else:
    print(f"You are not eligible to go to the Club:{age}")

# Step 4 Check for edge cases
#negative input
#non numeric value
#long

# Step 5 Optimize the code