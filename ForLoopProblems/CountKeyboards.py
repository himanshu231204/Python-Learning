"""   Count all letters, digits, and special symbols from a given 
string 
Given: str1 = "P@#yn26at^&i5ve" 
Expected Outcome: 
Total counts of chars, digits, and symbols 
Chars = 8 
Digits = 3 
Symbol = 4
"""

a="123#$(&hgtfd#$#87)"
chr=0
dig=0
spch=0
for i in a:
    if i.isdigit():
        dig+=1
    elif i.isalpha():
        chr+=1
    else:
        spch=0
print(f"digit {dig}\n alphabets {chr}\n special charcter {spch}")      