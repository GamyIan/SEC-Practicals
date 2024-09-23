# Create a user definined dictionary where key will be any given number and value is whether the number is prime or not

def isPrime(n):
    n=abs(n)
    if n==0 or n==1: return "Non-Prime"
    for i in range(2,n//2+1):
            if n%i==0: return "Non-Prime"
    return "Prime"
   
        
primes={}
keys=int(input("Enter number of keys: "))
for i in range(1,keys+1):
    n=int(input("Enter key value: "))
    primes[n]=isPrime(n)
    
print(f"Primes Dictionary = {primes}")

