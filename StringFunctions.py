 
text = "   hello python programming   "

print("Original String:", text)

# strip()
clean = text.strip()
print("After strip():", clean)

# upper()
print("Uppercase:", clean.upper())

# lower()
print("Lowercase:", clean.lower())

# title()
print("Title Case:", clean.title())

# replace()
print("Replace 'python' with 'java':", clean.replace("python", "java"))

# split()
words = clean.split(" ")
print("Split into list:", words)

# join()
joined = "-".join(words)
print("Joined with - :", joined)

# find()
print("Find 'python':", clean.find("python"))

# count()
print("Count of 'o':", clean.count("o"))

# startswith() , endswith()
print("Starts with 'hello'? :", clean.startswith("hello"))
print("Ends with 'programming'? :", clean.endswith("programming"))

# String Slicing
print("First 5 characters:", clean[:5])
print("Last 5 characters:", clean[-5:])

# f-string formatting
name = "Ishwar"
age = 22
print(f"My name is {name} and my age is {age}.")
