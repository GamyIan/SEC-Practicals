units=float(input("Enter number of units consumed: "))
bill=0
if 0<=units<=50:
    bill=units*0.5
elif units<=150:
    bill=25+(units-50)*0.75
elif units<=250:
    bill=100+(units-150)*1.2
elif 250<units:
    bill=220+(units-250)*1.5
else:
    print("Invalid Input")
    exit(0)

bill*=1.2
print(f"Total Bill: {bill:.2f}rs.")



