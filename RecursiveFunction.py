# Lambda function
square = lambda x: x * x
print("Square of 5:", square(5))

# Recursive function (Factorial)
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print("Factorial of 5:", fact(5))
