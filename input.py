# 1. String input
name = input("Enter your name: ")
print("Hello,", name)

# 2. Integer input
age = int(input("Enter your age: "))
print("You are", age, "years old")

# 3. Float input
height = float(input("Enter your height in meters: "))
print("Your height is", height, "meters")

# 4. Multiple inputs in one line (space-separated)
x, y = input("Enter two numbers separated by space: ").split()
x = int(x)
y = int(y)
print("Sum =", x + y)

# 5. Multiple inputs using map()
a, b = map(float, input("Enter two decimal numbers separated by space: ").split())
print("Sum of floats =", a + b)
