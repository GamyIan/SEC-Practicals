# Write a script to enter a user defined list and generae a prime list from the given list
def isPrime(n):
    n=abs(n)
    if n==1: return False
    elif n>1:
        for i in range(2,n//2+1):
            if n%i==0: return False
    return True

l=[]
primes=[]
n=int(input("Enter number of elements: "))
for i in range(n):
    l.append(int(input(f"Enter element {i+1}: ")))
    if isPrime(l[i]): primes.append(l[i])
    
print("Original List =",l)
print("Prime List =",primes)

