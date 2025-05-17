#Accept name and age from the user. Check if the user is a valid voter or not


name=input("Enter your Name :")
age=int(input("Enter your age :"))

if age>=18:
    print(f"Hello {name} you are a valid voter")
else:
    print(f"Hello {name} you are not a valid voter")   
