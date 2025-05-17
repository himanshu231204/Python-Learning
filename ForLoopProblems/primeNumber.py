n=int(input("check given number is prime or not "))
count=0
for i in range(1,n+1):
    if n%i==0:
        count=count+1
    
if count==2:
    print("Given number is prime number ")
else:
    print("Given number is not prime number ")