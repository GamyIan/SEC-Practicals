# Create a user defined dictionary where the key is a number and the value is the square of the number

sqrs={}
keys=int(input("Enter number of keys: "))
for i in range(1,keys+1):
    n=int(input("Enter key value: "))
    sqrs[n]=n**2
    
print(f"Sqaures Dictionary = {sqrs}")

