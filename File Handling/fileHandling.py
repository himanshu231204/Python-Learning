# ==============================================
# 📘 File Handling in Python
# ==============================================

# File handling allows reading from and writing to files.
# It uses built-in functions like open(), read(), write(), close(), etc.

# ==============================================
# 📁 File Modes
# ==============================================

"""
'r'   -> Read (default mode) - File must exist
'w'   -> Write - Overwrites file or creates new one
'a'   -> Append - Adds to the end of file
'x'   -> Create - Fails if file exists
'b'   -> Binary mode
't'   -> Text mode (default)
"""

# ==============================================
# 🔓 Opening a File
# ==============================================

file = open("example.txt", "w")  # opens in write mode
file.write("Hello, this is a test file!\n")
file.write("Adding another line.")
file.close()

# ==============================================
# 📖 Reading a File
# ==============================================

# 1. Read entire content
file = open("example.txt", "r")
content = file.read()
print("Content:\n", content)
file.close()

# 2. Read line by line
file = open("example.txt", "r")
for line in file:
    print("Line:", line.strip())
file.close()

# 3. Readlines() - returns list of lines
file = open("example.txt", "r")
lines = file.readlines()
print("Readlines Output:", lines)
file.close()

# ==============================================
# ✍️ Appending to a File
# ==============================================

file = open("example.txt", "a")
file.write("\nThis line is appended.")
file.close()

# ==============================================
# ✅ Using 'with' Statement (Recommended)
# ==============================================

# Automatically closes the file after block ends
with open("example.txt", "r") as f:
    data = f.read()
    print("\nData using with block:\n", data)

# ==============================================
# 📂 Working with Binary Files
# ==============================================

# Writing binary
with open("binary_file.bin", "wb") as f:
    f.write(b"This is binary data")

# Reading binary
with open("binary_file.bin", "rb") as f:
    binary_data = f.read()
    print("Binary Data:", binary_data)

# ==============================================
# 🚫 File Not Found Error Handling
# ==============================================

try:
    f = open("non_existent.txt", "r")
except FileNotFoundError:
    print("❌ The file was not found.")

# ==============================================
# 🔄 File Methods Summary
# ==============================================

"""
file.read([n])       -> Read n characters or entire file
file.readline()      -> Read one line
file.readlines()     -> Read all lines as a list
file.write(str)      -> Write a string to file
file.writelines(list)-> Write a list of strings
file.seek(n)         -> Move cursor to nth byte
file.tell()          -> Returns current position
file.close()         -> Closes the file
"""

# ==============================================
# ✅ Best Practices
# ==============================================

"""
- Always close the file using close() or 'with' block
- Use 'with open(...)' for automatic closing
- Handle FileNotFoundError using try-except
- Use binary modes when working with images or media files
"""
