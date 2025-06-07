starting_salary=int(input("Enter the starting salary: "))
percentage_increase=int(input("Enter the percentage increase in salary: "))
years=int(input("Enter the number of years: "))

print("Year       Salary")
print("\n")

salary =starting_salary
for year in range(1,years + 1):
    print(str(year)+ "         "+str(round(salary,2)))
    salary=salary+(salary*(percentage_increase/100))