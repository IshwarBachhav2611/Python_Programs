# Variable-length arguments (*args)
def total(*nums):
    print("Total =", sum(nums))

# Keyword variable-length arguments (**kwargs)
def info(**details):
    print("Details:", details)

# Nested function
def outer():
    print("This is outer function")
    
    def inner():
        print("This is inner function")
    
    inner()  # calling nested function


# Calling all
total(10, 20, 30)
info(name="Ishwar", age=22, city="Nashik")
outer()
