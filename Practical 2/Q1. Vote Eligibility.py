# Q1 - Vote Eligibility
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