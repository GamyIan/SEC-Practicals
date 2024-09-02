# Q2
# Write a program to accept two inputs: upper and lower limit 
# and print all the odd and even between the given range


lower=int(input("Lower Limit: "))
upper=int(input("Upper Limit: "))
even="Even: "
odd="Odd: "
if lower<=upper:
    for i in range(lower,upper+1):
        if i%2==0:
            even+=str(i)+" "
        else:
            odd+=str(i)+" "
else:
    print("Invalid Input")

print(even)
print(odd)
    
