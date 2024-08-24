# Taking basic information from user
roll=int(input("Enter Roll number: "))
name=input("Enter Name: ")

print("Enter marks out of 100 in the following subjects:")

# Accepting Marks from user
major=int(input("Major: "))
minor=int(input("Minor: "))
oe1=int(input("OE1: "))
oe2=int(input("OE2: "))

# Calculating %
per=(major+minor+oe1+oe2)/4

# Displaying output
print(f"Roll number: {roll}")
print(f"Name: {name}")
print(f"Percentage: {per:.2f}%")