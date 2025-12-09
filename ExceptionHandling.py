try:
    #Code that may cause error
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2

    #Accessing list index (may cause IndexError)
    nums = [10, 20, 30]
    print(nums[5])  # This will cause IndexError

except ZeroDivisionError:
    print("You cannot divide by ZERO!")

except ValueError:
    print("Invalid input! Please enter numbers only.")

except IndexError:
    print("List index out of range!")

except Exception as e:
    print(f"Some other error occurred: {e}")

else:
    # Runs ONLY if no exception occurs
    print(f"Division successful! Result = {result}")

finally:
    # Always runs
    print("Program finished (finally block executed)")

# Raising your own exception
age = int(input("Enter your age: "))

if age < 18:
    raise Exception("! Age must be 18 or above!")
else:
    print("You are eligible!")
