initial_height = float(input("Enter the initial height (in feet): "))
bounciness_index = float(input("Enter the bounciness index (e.g., 0.6): "))
num_bounces = int(input("Enter the number of bounces: "))
total_distance = initial_height
height = initial_height
for i in range(num_bounces):
    height *= bounciness_index
    total_distance += 2 * height  
print("Total distance traveled by the ball:", round(total_distance, 2), "feet")
