def fact(n):
    fact=1
    for i in range(2,n+1):
        fact*=i
    return fact

num=int(input("Enter Number: "))
if num>=0:
    print(f"{num}! = {fact(num)}")
else:
    print("Please enter a positive number")