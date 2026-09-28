# =====================================================
#        EXCEPTION HANDLING IN PYTHON
# =====================================================

# User-defined exception
class AgeError(Exception):
    pass


try:
    # Taking input from user
    age = int(input("Enter your age: "))

    # -------------------------------
    # Built-in exception using raise
    # -------------------------------
    if age < 0:
        raise ValueError("Age cannot be negative")

    # -------------------------------
    # User-defined exception
    # -------------------------------
    if age < 18:
        raise AgeError("Age must be 18 or above")

    # Division example
    number = int(input("Enter a number: "))
    result = 100 / number

except ValueError as e:
    # Handles invalid integer input
    print("ValueError:", e)

except AgeError as e:
    # Handles our custom exception
    print("AgeError:", e)

except ZeroDivisionError as e:
    # Handles division by zero
    print("ZeroDivisionError:", e)

except Exception as e:
    # Handles any other unexpected exception
    print("Some other error:", e)

else:
    # Runs only when there is NO exception
    print("No exception occurred.")
    print("Result:", result)

finally:
    # Always executes
    print("Finally block executed.")
    print("Program completed.")