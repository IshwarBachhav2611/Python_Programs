# 1. Creating a list
fruits = ["apple", "banana", "cherry"]
print("Original list:", fruits)

# 2. Accessing elements (indexing)
print("First fruit:", fruits[0])
print("Last fruit:", fruits[-1])

# 3. Slicing
print("Slice fruits[0:2]:", fruits[0:2])

# 4. Modifying elements
fruits[1] = "orange"
print("After modification:", fruits)

# 5. Adding elements
fruits.append("mango")       
fruits.insert(1, "kiwi")     
print("After adding elements:", fruits)

# 6. Removing elements
fruits.remove("cherry")      
popped = fruits.pop()        
print("After removing elements:", fruits)
print("Popped element:", popped)

# 7. List length
print("Length of list:", len(fruits))

# 8. Searching elements
print("Is 'apple' in list?", "apple" in fruits)

# 9. Sorting
numbers = [4, 1, 7, 3]
numbers.sort()
print("Sorted numbers:", numbers)
numbers.sort(reverse=True)
print("Reverse sorted numbers:", numbers)

# 10. Reversing a list
fruits.reverse()
print("Reversed fruits:", fruits)

# 11. Copying a list
fruits_copy = fruits.copy()
print("Copy of fruits:", fruits_copy)

# 12. Clearing a list
fruits_copy.clear()
print("Cleared copy:", fruits_copy)
