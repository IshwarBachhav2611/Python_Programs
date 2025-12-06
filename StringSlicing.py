text = "Hello, Python!"

# 1. Basic slicing: text[start:end] (end is not included)
print("text[0:5] ->", text[0:5])   # 'Hello'

# 2. Slicing from start to a position
print("text[:5] ->", text[:5])     # 'Hello'

# 3. Slicing from a position to end
print("text[7:] ->", text[7:])     # 'Python!'

# 4. Negative indexing (from end)
print("text[-7:-1] ->", text[-7:-1])  # 'Python'

# 5. Skipping characters with step: text[start:end:step]
print("text[0:12:2] ->", text[0:12:2])  # 'Hlo y'

# 6. Reverse a string using slicing
print("text[::-1] ->", text[::-1])       # '!nohtyP ,olleH'
