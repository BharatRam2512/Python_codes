def total_rent(new, old):
    rent1=(new*3)+(old*2)
    return rent1    
new=int(input("Enter the number of new DVDs rented: "))
old=int(input("Enter the number of old DVDs rented: "))
print("The total rent is: $", total_rent(new, old))