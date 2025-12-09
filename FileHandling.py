# 1. Writing to a file (w mode)
with open("demo.txt", "w") as f:
    f.write("Hello Ishwar!\n")
    f.write("Welcome to Python file handling.\n")

print("Writing done!")

# 2. Appending to a file (a mode)
with open("demo.txt", "a") as f:
    f.write("This text is appended.\n")

print("Append done!")
  
# 3. Reading the entire file (r mode)
with open("demo.txt", "r") as f:
    data = f.read()
    print("\n--- File Content (read) ---")
    print(data)

# 4. Reading line by line
with open("demo.txt", "r") as f:
    print("--- Reading Line by Line ---")
    for line in f:
        print(line.strip())

# 5. Using readline()
with open("demo.txt", "r") as f:
    print("\nFirst line:", f.readline().strip())
    print("Second line:", f.readline().strip())

# 6. Using readlines() → gives list of lines
with open("demo.txt", "r") as f:
    lines = f.readlines()
    print("\nList of lines:", lines)

# 7. Checking file exists (error handling)
try:
    with open("unknown.txt", "r") as f:
        print(f.read())
except FileNotFoundError:
    print("\nFile not found error handled!")

