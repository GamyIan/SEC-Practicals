# Create a program that allows a user to store, search and delete contacts. 
# Each contact should have a name and a phone number.
# Implement the following functions:
# add(name, phone), search(name), delete(name), list()
# The program should be menu driven

contacts={}
def add():
    name=input("Enter Name: ")
    phone=int(input("Enter Phone number: "))
    contacts[name]=phone

def rem():
    name=input("Enter Name: ")
    if name in contacts:
        contacts.pop(name)
        print(f"{name} was removed.")
    else:
        print("Contact doesn't exist.")

def find():
    name=input("Enter Name: ")
    if name in contacts:
        print(f"Name: {name}\nPhone: {contacts[name]}")
    else:
        print("Contact not found.")
        print("Do you want to create a contact? (yes or no)")
        inp=input("Input: ").lower()
        if inp=="yes": add()

def show():
    print("Contacts:")
    for name in contacts:
        print(f"{name}: {contacts[name]}")

print("Phonebook Application:")
print("add: Add a contact")
print("rem: Remove a contact")
print("find: Find a contact")
print("show: Show all contacts")
print("exit: Exit the program")

inp=""
while inp!="exit":
    inp=input("Input: ").lower()
    match inp:
        case "add": add(),
        case "rem": rem(),
        case "find": find(),
        case "show": show()
    print()
    
    
