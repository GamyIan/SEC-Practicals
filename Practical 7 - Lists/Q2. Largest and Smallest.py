# Write a program to give the largest and smallest number from a user definied list
l=[]
n=int(input("Enter number of elements: "))
for i in range(n):
    l.append(int(input(f"Enter element {i+1}: ")))
    
big=l[0]
smol=l[0]

for num in l:
    if num>big: big=num
    elif num<smol: smol=num
    
print("List =",l)
print(f"Largest = {big}")
print(f"Smallest = {smol}")