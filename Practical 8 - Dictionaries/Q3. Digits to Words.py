# Create a user definied dictionary where key will be a number and value will be the number in digits
# For eg (420, "FourTwoZero")

# List with words and indexes linked
words=["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]

# Returns the digits of number in figures. 
def toFig(n):
    n=abs(n)
    figure=""
    while n>0:
        figure=words[n%10]+figure
        n=n//10
    return figure

# Creating the dictionary
worded_digits={}

keys=int(input("Enter number of keys: "))
for i in range(1,keys+1):
    n=int(input("Enter key value: "))
    worded_digits[n]=toFig(n)
    
print(f"Digits in Words: {worded_digits}")

