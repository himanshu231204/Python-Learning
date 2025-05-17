n=int(input("Is given number is perfect number"))
sum=0
for i in range(1,n):
    if n%i==0:
        sum=sum+i
        
if sum==n:
    print("Yes it is perfect")
else:
    print("Not a perfect number")
            
           