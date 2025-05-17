import random

num=random.randint(1,10)

tries=0

while True:
        guess= int(input(" Guess your number"))


        if num==guess:
                tries+=1
                print(" you are right ,you gussed the number is {tries} tries")
               
                print("you are right")
                break

        elif num<guess:
              print("go a littel lower")
              tries+=1

        elif num>guess:
               print("go a littel higher")
               tries+=1
               
        
                          
        else:
          tries+=1
          print("Sorry you are wrong")


    
    