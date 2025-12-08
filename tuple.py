# 1. Creating a tuple
numbers = (10, 20, 30, 40, 20)
print("Original Tuple:", numbers)

# 2. Accessing elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])

# 3. Slicing
print("Slice numbers[1:4]:", numbers[1:4])
print("Slice with negative index:", numbers[-4:-1])

# 4. Tuple methods
print("Count of 20:", numbers.count(20))
print("Index of 30:", numbers.index(30))

# 5. Packing (automatic tuple creation)
packed = 1, "Python", 3.14
print("Packed Tuple:", packed)

# 6. Unpacking
a, b, c = packed
print("Unpacked Values:", a, b, c)

# 7. Nested tuple
nested = (1, 2, (3, 4, 5))
print("Nested Tuple:", nested)
print("Access 4 inside nested:", nested[2][1])

# 8. Looping through tuple
print("\nLooping:")
for item in numbers:
    print(item)

# 9. Converting tuple to list (to modify)
temp_list = list(numbers)
temp_list.append(100)
print("After converting to list and modifying:", temp_list)

# 10. Converting back to tuple
new_tuple = tuple(temp_list)
print("Converted back to tuple:", new_tuple)
