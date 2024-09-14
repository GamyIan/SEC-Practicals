# Q1. Write a python script to print sum of prime digits in a given number

def isPrime(n):
    n=abs(n)
    if n==1: return 0
    elif n>1:
        for i in range(2,n//2+1):
            if n%i==0: return 0
    return n


n=int(input("Enter number: "))
sum=0
while n>0:
    sum+=isPrime(n%10)
    n=n//10

print("Sum of prime digits =", sum)

