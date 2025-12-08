# 1. Creating a dictionary
student = {
    "name": "Ishwar",
    "age": 22,
    "course": "Python",
    "marks": 85
}
print("Original Dictionary:", student)

# 2. Accessing values
print("Name:", student["name"])
print("Age:", student.get("age"))  

# 3. Adding new key-value
student["city"] = "Nashik"
print("After adding city:", student)

# 4. Updating values
student["marks"] = 90
student.update({"course": "Data Science"})
print("After update:", student)

# 5. Removing items
student.pop("age")        
print("After pop(age):", student)

student.popitem()        
print("After popitem():", student)

del student["city"]       
print("After del city:", student)

# 6. Dictionary keys, values, items
print("Keys:", student.keys())
print("Values:", student.values())
print("Items:", student.items())

# 7. Looping in dictionary
print("\nLooping through dictionary:")
for key, value in student.items():
    print(key, ":", value)

# 8. Nested dictionary
class_data = {
    "stud1": {"name": "Ishwar", "marks": 90},
    "stud2": {"name": "Rohan", "marks": 85}
}
print("\nNested Dictionary:", class_data)
print("Marks of stud1:", class_data["stud1"]["marks"])

# 9. Copying and clearing
copy_data = student.copy()
print("Copied dictionary:", copy_data)

copy_data.clear()
print("After clearing copy:", copy_data)
