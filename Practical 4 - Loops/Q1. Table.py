# Q1 Print tables of a number upto a certain limit

def table(n,l):
    for i in range(1,l+1):
        print(f"{n}*{i} = {n*i}")



n=input("Enter number: ")
limit=int(input("Enter limit: "))
if n.isdigit():
    table(int(n),limit)
else:
    if n[0]=='-' and n[1:].isdigit():
        print("Converting number to positive")
        table(int(n[1:]),limit)
    else:
        print("Invalid input, only numbers allowed")

print("End of program")

