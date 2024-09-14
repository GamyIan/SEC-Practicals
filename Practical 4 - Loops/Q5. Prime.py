def isPrime(n):
    n=abs(n)
    if n==1: return False
    elif n>1:
        for i in range(2,n//2+1):
            if n%i==0: return False
    return True

num=int(input("Enter number: "))
if isPrime(num): print(f"{num} is a Prime number.")
else: print(f"{num} is not a Prime number.")

