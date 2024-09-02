# Q2. Write a python script to check whether a given number is a palindrome or not

def rev(n):
    r=0
    while n>0:
        r=r*10+(n%10)
        n=n//10
    return r


n=int(input("Enter number: "))
if n==rev(n):
    print("Palindrome")
else:
    print("Not Palindrome")
    
