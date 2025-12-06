# Simple function
def greet():
    print("Hello from greet()!")

# Function with parameters
def add(a, b):
    return a + b

# Function with default argument
def welcome(name="Guest"):
    print("Welcome", name)

# Function with keyword arguments
def student(name, age):
    print("Name:", name, "Age:", age)

# Function returning multiple values
def calc(a, b):
    return a + b, a - b, a * b


# Calling all
greet()
print("Addition:", add(5, 10))
welcome()
welcome("Ishwar")
student(age=21, name="Rahul")
x, y, z = calc(10, 5)
print("Results:", x, y, z)
