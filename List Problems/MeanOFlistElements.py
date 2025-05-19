# Mean of List elements

ls=[1,2,3,4,5,]

sum=0
for i in range(len(ls)):
    sum=sum+ls[i]

median=sum//len(ls)
print(f"The median of list elements is {median}")

