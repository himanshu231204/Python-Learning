# find the second largest elements in list and print it index

ls=[1,2,7,10,4,5,9]

largest=ls[0]
sec_largest=ls[0]
index=0
for i in range(len(ls)):
    if largest<ls[i]:
        sec_largest=largest
        largest=ls[i]
      
    elif ls[i]>sec_largest & ls[i]!=largest:
            sec_largest=ls[i]
         
print(sec_largest)