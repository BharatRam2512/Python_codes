initail_population=int(input("Enter the initial population: "))
growth_rate = int(input("Enter the growth rate (as a percentage): "))
hours_per_growth = int(input("Enter the number of hours per growth period: "))
total_hours = int(input("Enter the total number of hours: "))
growth_periods = total_hours // hours_per_growth
population=initail_population*(growth_rate**growth_periods)
print(f"The population after {total_hours} hours will be: {population}")