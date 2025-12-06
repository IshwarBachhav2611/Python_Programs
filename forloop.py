print("1) Simple for loop using range:")
for i in range(1, 6):
    print(i)

print("\n2) Looping through a list:")
colors = ["red", "blue", "green"]
for c in colors:
    print(c)

print("\n3) Looping through a string:")
name = "PYTHON"
for ch in name:
    print(ch)

print("\n4) Using break in for loop:")
for i in range(1, 10):
    if i == 5:
        break
    print(i)

print("\n5) Using continue in for loop:")
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

print("\n6) Using pass in for loop:")
for i in range(3):
    pass   # placeholder
print("Pass executed (no action).")

print("\n7) For loop with else:")
for i in range(1, 4):
    print(i)
else:
    print("For loop finished without break!")
