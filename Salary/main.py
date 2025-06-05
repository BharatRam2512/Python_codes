hourly_wages=int(input("enter the value: ")) 
regular_hours=int(input("enter the value: ")) 
overtime_hours=int(input("enter the value: ")) 
overtime_pay=overtime_hours*(1.5*regular_hours) 
weekly_pay=hourly_wages*regular_hours+overtime_pay 
print(weekly_pay) 