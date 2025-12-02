# Variables
name = "Ishwar"
age = 21
height = 5.8
marks = 92.5

# Basic f-string
print(f"My name is {name} and I am {age} years old.")

# f-string with arithmetic
print(f"Next year, I will be {age + 1} years old.")

# f-string with float formatting (2 decimal places)
print(f"My height is {height:.2f} meters.")  

# f-string with padding and alignment
print(f"{'Name':<10} {'Age':<5} {'Marks':<6}")   
print(f"{name:<10} {age:<5} {marks:<6.2f}")    

# f-string with expressions
print(f"Half of my marks is {marks / 2}")
