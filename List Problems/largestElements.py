#Find the greatest element and print its index too

ls=[1,2,7,10,4,5]

largest=ls[0]
index=0
for i in range(len(ls)):
    if largest<ls[i]:
        largest=ls[i]
        index=i

print(largest)
print(index)