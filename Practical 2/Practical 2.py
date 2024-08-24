# Practical 2:
# Conditional statements

# Q1 - Vote Eligibility
def Q1():
    name=input("Enter Name: ").title()
    citizen=input("Enter 'yes' if you're indian and 'no' if not: ").lower()
    if citizen=='yes':
        age=int(input("Enter your age: "))
        if age>=18:
            print(f"{name} you are Eligible to vote!")
        else:
            print(f"Sorry {name} you are under 18!")
    else:
        print(f"Sorry {name} you need to be a citizen of India.")

# Q2 - Categorising a Number
def Q2():
    n=int(input("Enter number: "))
    remainder=n%2
    if n==0:
        print("The number is 0")
    elif n>0:
        if remainder==0:
            print(f"{n} is a Positive Even Integer")
        else:
            print(f"{n} is a Positive Odd Integer")
    else:
        if remainder==0:
            print(f"{n} is a Negative Even Integer")
        else:
            print(f"{n} is a Negative Odd Integer")

# Q3 - Greatest of 3 numbers
def Q3():
    n1=int(input("Enter number 1: "))
    n2=int(input("Enter number 2: "))
    n3=int(input("Enter number 3: "))
    
    if n1==n2==n3:
        print("All numbers are the same.")
    elif n1<n2:
        if n2==n3:
            print("Numbers 2 and 3 are the greatest.")
        elif n2<n3:
            print("Number 3 is greatest.")
        else:
            print("Number 2 is greatest.")
    elif n1<n3:
        if n3==n2:
            print("Numbers 2 and 3 are the greatest.")
        elif n3<n2:
            print("Number 2 is greatest.")
        else:
            print("Number 3 is greatest.")
    else:
        if n1==n3:
            print("Numbers 1 and 3 are the greatest.")
        elif n1==n2:
            print("Numbers 1 and 2 are the greatest.")
        else:
            print("Number 1 is the greatest.")

Q1()
Q2()
Q3()