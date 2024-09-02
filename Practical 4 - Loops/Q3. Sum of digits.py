# Print sum of digits of a number

n=input("Enter number: ")
sum=0
# For Loop
if n.isdigit():
    for i in n:
        sum+=int(i)
else:
    if n[0]=='-' and n[1:].isdigit():
        print("Converting number to positive")
        for i in n[1:]:
            sum+=int(i)
    else:
        print("Invalid input")

print(f"Sum: {sum} (For Loop)")

# While Loop
sum=0
n=int(n)
while n>0:
    sum+=n%10
    n=n//10
print(f"Sum: {sum} (While Loop)")