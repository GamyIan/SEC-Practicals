# Write  a program to sort a given list

l=[]
sort=[]
n=int(input("Enter number of elements: "))
for i in range(n):
    l.append(int(input(f"Enter element {i+1}: ")))


size=len(l)

for i in range(size):
    smol=l[i]
    for num in l[i:]:
        if num<smol:
            smol=num
    l.remove(smol)  
    sort.append(smol)
    
print("Original List",l)
print("Sorted List",sort)