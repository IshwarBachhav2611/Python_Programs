# 1. Creating dictionary
student = {
    "name": "Ishwar",
    "age": 22,
    "course": "MCA",
    "marks": {"math": 90, "python": 95},
    "skills": ["Python", "Java", "SQL"]
}

print("Original Dictionary:")
print(student)


# 2. Accessing values
print("Access name:", student["name"])
print("Access Python marks:", student["marks"]["python"])
print("Access skills list:", student["skills"])
print("Access using get():", student.get("age"))


# 3. Adding elements
student["city"] = "Nashik"
student["graduated"] = False
print("After Adding items:", student)


# 4. Updating values
student["age"] = 23
student["skills"].append("Django")
print("After Updating items:", student)


# 5. Removing items
student.pop("city")         
student.popitem()           
del student["course"]
print("After Removing items:", student)


# 6. Looping in Dictionary
print("Loop: Keys")
for key in student.keys():
    print(key)

print("Loop: Values")
for value in student.values():
    print(value)

print("Loop: Key & Value")
for key, value in student.items():
    print(key, ":", value)


# 7. Dictionary Methods
print("All Keys:", student.keys())
print("All Values:", student.values())
print("All Items:", student.items())

clone = student.copy()
print("Copy of Dictionary:", clone)

student.update({"country": "India"})
print("After update():", student)


# 8. Nested Dictionary
college = {
    "student1": {"name": "Amit", "age": 21},
    "student2": {"name": "Ishwar", "age": 22}
}
print("Nested Dictionary:", college)
print("Access nested value:", college["student2"]["name"])
