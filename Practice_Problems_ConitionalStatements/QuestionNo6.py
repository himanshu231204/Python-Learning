#take the input of temperatuer in celsius
"""
 Below 0°C → "Freezing Cold 
0°C to 10°C → "Very Cold 
10°C to 20°C → "Cold 
20°C to 30°C → "Pleasant 
30°C to 40°C → "Hot 
Above 40°C → "Very Hot "

"""

temp=int(input("Enter the temperatuer : "))

if temp<0:
    print("Freezing Cold")
elif temp>=0 and temp<=10:
    print("Very cold")
elif temp>=10 and temp<=20:
    print("Cold")
elif temp>=20 and temp<=30:
    print("Pleasant")
elif temp>=30 and temp<=40:
    print("Hot")
else:
    print("Very hot")