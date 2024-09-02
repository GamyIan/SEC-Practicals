# Q2 - Categorising a Number
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