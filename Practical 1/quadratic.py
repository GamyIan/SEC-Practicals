# Find roots of a quadratic equation
from math import sqrt
from cmath import sqrt as csqrt
print("Bring quadratic equation in the standard form:")
print("ax²+bx+c=0")
a=int(input("Enter a: "))
b=int(input("Enter b: "))
c=int(input("Enter c: "))
D=b**2-4*a*c

print(f"\nDiscriminant: {D}")

if D==0:
    print("Equation has real and unique root")
    print(f"Root: {-b/(2*a)}")
elif D<0:
    print("Equation has imaginary roots")
    print(f"Roots: {(-b+csqrt(D))/(2*a)} and {(-b-csqrt(D))/(2*a)}")
else:
    print("Equation has real and distinct roots")
    print(f"Roots: {(-b+sqrt(D))/(2*a)} and {(-b-sqrt(D))/(2*a)}")
    
