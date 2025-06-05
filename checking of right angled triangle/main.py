side1=int(input("Enter the length of the first side: "))
side2=int(input("Enter the length of the second side: "))
side3=int(input("Enter the length of the third side: "))
x=sorted([side1, side2, side3])
if x[2]**2 == x[0]**2+ x[1]**2:
    print("The triangle is right-angled.")
else:
    print("The triangle is not right-angled.")