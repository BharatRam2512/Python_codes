standard_deduction = 10000
additional_deduction = 3000
gross = int(input("Enter your gross income: "))
dependent = int(input("Enter the number of dependents: "))
tax=(gross-standard_deduction-(additional_deduction*dependent))*0.2
print(tax)