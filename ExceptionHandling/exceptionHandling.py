# ==============================================
# 📘 Exception Handling in Python
# ==============================================

# ✅ What is an Exception?
# An exception is an error that occurs during program execution.
# It interrupts the normal flow of the program.

# ==============================================
# ⚠️ Types of Errors
# ==============================================

# 1. Syntax Error Example
# if x > 5
#     print("Hello")  # SyntaxError: missing colon

# 2. Runtime Error (Exception)
# a = 5 / 0  # ZeroDivisionError

# ==============================================
# 🛠 Why Handle Exceptions?
# ==============================================
# - Prevent program from crashing
# - Show meaningful error messages
# - Improve user experience

# ==============================================
# 🔐 Try-Except Block
# ==============================================

try:
    # Risky code
    a = int(input("Enter a number: "))
    result = 10 / a
    print("Result:", result)
except ZeroDivisionError:
    print("❌ Cannot divide by zero!")
except ValueError:
    print("❌ Invalid input! Please enter a valid integer.")

# ==============================================
# 🧱 Else Clause
# ==============================================

try:
    print("Inside try block")
except:
    print("An error occurred")
else:
    print("No error occurred! This is the else block.")

# ==============================================
# 🧹 Finally Clause
# ==============================================

try:
    x = 10
    print("Try block executed")
except:
    print("Error occurred")
finally:
    print("This block always executes (finally)")

# ==============================================
# ✏️ Raising Exceptions Manually
# ==============================================

# raise ValueError("Manually raised error!")

# ==============================================
# ✅ Catching Multiple Exceptions Together
# ==============================================

try:
    a = int(input("Enter number: "))
    b = 5 / a
except (ValueError, ZeroDivisionError) as e:
    print("Error occurred:", e)

# ==============================================
# ✅ Custom Exception Example
# ==============================================

class NegativeNumberError(Exception):
    pass

num = -10
if num < 0:
    raise NegativeNumberError("❌ Negative numbers are not allowed!")

# ==============================================
# 📚 Common Built-in Exceptions
# ==============================================

"""
ZeroDivisionError     => Division by zero
ValueError            => Invalid value passed
TypeError             => Operation on incompatible types
IndexError            => List index out of range
KeyError              => Dictionary key not found
FileNotFoundError     => File not found
NameError             => Variable not defined
"""

# ==============================================
# ✅ Best Practices
# ==============================================
# - Always catch specific exceptions
# - Avoid using bare 'except:' unless absolutely necessary
# - Use finally to release resources (e.g., closing files or DB)
# - Avoid hiding errors (don't silence all exceptions)
