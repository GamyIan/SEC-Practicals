# Q3 - Greatest of 3 numbers
n1=int(input("Enter number 1: "))
n2=int(input("Enter number 2: "))
n3=int(input("Enter number 3: "))

if n1==n2==n3:
    print("All numbers are the same.")
elif n1<n2:
    if n2==n3:
        print(f"Numbers {n2} and {n3} are the greatest.")
    elif n2<n3:
        print(f"Number {n3} is greatest.")
    else:
        print(f"Number {n2} is greatest.")
elif n1<n3:
    if n3==n2:
        print(f"Numbers {n2} and {n3} are the greatest.")
    elif n3<n2:
        print(f"Number {n2} is greatest.")
    else:
        print(f"Number {n3} is greatest.")
else:
    if n1==n3:
        print(f"Numbers {n1} and {n3} are the greatest.")
    elif n1==n2:
        print(f"Numbers {n1} and {n2} are the greatest.")
    else:
        print(f"Number {n1} is the greatest.")