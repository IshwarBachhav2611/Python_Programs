a = 10           # int
b = 12.5         # float
c = "100"        # string (numeric)
d = True         # boolean

print("----- Convert TO INT -----")
print(int(b))    # float → int
print(int(c))    # string → int
print(int(d))    # bool → int

print("\n----- Convert TO FLOAT -----")
print(float(a))  # int → float
print(float(c))  # string → float
print(float(d))  # bool → float

print("\n----- Convert TO STRING -----")
print(str(a))    # int → string
print(str(b))    # float → string
print(str(d))    # bool → string

print("\n----- Convert TO BOOLEAN -----")
print(bool(a))   # int → bool
print(bool(0))   # int → bool
print(bool(c))   # string → bool
print(bool(""))  # empty string → bool
