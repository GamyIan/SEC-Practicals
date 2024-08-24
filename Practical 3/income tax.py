salary=float(input("Enter Annual Salary: "))
Tax=0
if 0<=salary<=3*10**5:
    pass
elif 3*10**5<salary<=6*10**5:
    Tax=salary*0.05
elif salary<=9*10**5:
    Tax=15000+(salary-3*10**5)*0.1
elif salary<=12*10**5:
    Tax=45000+(salary-9*10**5)*0.15
elif salary<=15*10**5:
    Tax=90000+(salary-12*10**5)*0.2
elif 15*10**5<salary:
    Tax=1.5*10**5+(salary-15*10**5)*0.3
else:
    print("Invalid Input")
    exit(0)

#print(f"Gross Income: {salary}rs.")
print(f"Total Tax: {Tax}rs.")
print(f"Net Income: {salary-Tax}rs.")