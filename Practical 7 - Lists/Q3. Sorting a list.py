# Write  a program to sort a user defined list

l=[]
n=int(input("Enter number of elements: "))
for i in range(n):
    l.append(int(input(f"Enter element {i+1}: ")))

print("Original List",l)

for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[j]<l[i]:
            temp=l[i]
            l[i]=l[j]
            l[j]=temp

print("Sorted List",l)

