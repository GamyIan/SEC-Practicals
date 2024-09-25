# Create a program that allows a user to store, search and delete contacts. 
# Each contact should have a name and a phone number.
# Implement the following functions:
# add(name, phone), search(name), delete(name), list()
# The program should be menu driven

from platform import system as plat
from os import system

contacts={}

def clear():
    match plat():
        case "Windows": system("cls")
        case "Linux": system("clear")
        case _:
            print("Operating system not supported.")
            exit(1)

def add():
    clear()
    name=input("Enter Name: ")
    phone=int(input("Enter Phone number: "))
    contacts[name]=phone
    inp=input("Press any key to continue: ")
    clear()

def rem():
    clear()
    name=input("Enter Name: ")
    if name in contacts:
        contacts.pop(name)
        print(f"{name} was removed.")
    else:
        print("Contact doesn't exist.")
    inp=input("Press any key to continue: ")
    clear()

def find():
    clear()
    name=input("Enter Name: ")
    if name in contacts:
        print(f"Name: {name}\nPhone: {contacts[name]}")
    else:
        print("Contact not found.")
        print("Do you want to create a contact? (yes or no)")
        inp=input("Input: ").lower()
        if inp=="yes": add()
    inp=input("Press any key to continue: ")
    clear()
    

def show():
    clear()
    print("Contacts:")
    for name in contacts:
        print(f"{name}: {contacts[name]}")
    inp=input("Press any key to continue: ")
    clear()

def menu():
    print("Phonebook Application:")
    print("add: Add a contact")
    print("rem: Remove a contact")
    print("find: Find a contact")
    print("show: Show all contacts")
    print("exit: Exit the program")

inp=""
while inp!="exit":
    menu()
    inp=input("Input: ").lower()
    match inp:
        case "add":add(),
        case "rem": rem(),
        case "find": find(),
        case "show": show(),
        case "exit": print("Exiting the program...")
        case _: print("Invalid Input...")
    
