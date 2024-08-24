def isPrime(n):
    for i in range(2,n):
        if n%i==0: return False
    return True

num=int(input("Enter number: "))
if isPrime(num): print(f"{num} is a Prime number.")
else: print(f"{num} is not a Prime number.")

