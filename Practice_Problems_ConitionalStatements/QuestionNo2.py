#  Accept the gender from the user as char and print the respective greeting message

# Accept gender from the user
gender = input("Enter your gender (M/F): ").strip().upper()

# Check and print greeting message
if gender == 'M':
    print("Hello, Sir!")
elif gender == 'F':
    print("Hello, Ma'am!")
else:
    print("Invalid input. Please enter 'M' for Male or 'F' for Female.")


