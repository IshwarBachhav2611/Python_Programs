# 1. Creating sets
fruits = {"apple", "banana", "cherry"}
numbers = {1, 2, 3, 4, 4}  # duplicates automatically removed
print("Fruits set:", fruits)
print("Numbers set:", numbers)

# 2. Adding elements
fruits.add("orange")           # add single element
fruits.update(["mango", "kiwi"])  # add multiple elements
print("After adding elements:", fruits)

# 3. Removing elements
fruits.remove("banana")   # raises error if not present
fruits.discard("grape")   # no error if element not present
popped_item = fruits.pop()  # removes arbitrary element
print("After removing elements:", fruits)
print("Popped item:", popped_item)

# 4. Set operations
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("A union B:", A | B)         # {1,2,3,4,5,6}
print("A intersection B:", A & B)  # {3,4}
print("A difference B:", A - B)    # {1,2}
print("A symmetric difference B:", A ^ B)  # {1,2,5,6}

# 5. Checking membership
print("Is 3 in A?", 3 in A)
print("Is 5 not in A?", 5 not in A)

# 6. Length of a set
print("Length of set A:", len(A))

# 7. Clearing and copying
B_copy = B.copy()
B_copy.clear()
print("Cleared copy of B:", B_copy)
