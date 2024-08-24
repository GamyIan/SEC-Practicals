#5a
print("Q5A:")
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print() 
print()

# in a straight forward loop, 1 is added to i, ie 1,i+1
# while for a reverse loop i is subtract 1 from i ie 1,i-1,-1

#5b
print("Q5B:")
for i in range(1,6):
    for j in range(5,i-1,-1):
        print(j,end=" ")
    print()
print()

#5c
print("Q5C:")
k=0
for i in range(1,6):
    for j in range(1,i+1):
        k=k+1
        print(k,end=" ")
    print()
print()

#5d
print("Q5D:")
c=ord('A')
for i in range(1,5):
    for j in range(1,i+1):
        print(chr(c),end=" ")
        c=c+1
    print()