print("\n1) Simple while loop:")
x = 1
while x <= 5:
    print(x)
    x += 1

print("\n2) While loop with break:")
y = 1
while y <= 10:
    if y == 6:
        break
    print(y)
    y += 1

print("\n3) While loop with continue:")
z = 0
while z < 5:
    z += 1
    if z == 3:
        continue
    print(z)

print("\n4) While loop with pass:")
count = 0
while count < 3:
    pass  # nothing happens
    count += 1
print("Pass executed successfully!")

print("\n5) While loop with else:")
k = 1
while k <= 3:
    print(k)
    k += 1
else:
    print("While loop ended normally (no break).")
