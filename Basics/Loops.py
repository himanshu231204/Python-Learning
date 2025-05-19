# For Loops

"""
      Before understanding for loops you should know how range 
function works
 The range() function is used to generate a sequence of 
numbers, which is commonly used in loops

    Syntax of range function is simple range(start, stop, steps)
    
     you have 3 points from where you want to start, till where 
you want to stop and how many steps you want

   If you don’t mention start point the default value will be 0 .
 if you don’t mention the steps the default steps will be 1.
 you have to mention the stop point otherwise the range 
function will not work.
    """

# loops for numbers
    # syntax
for i in range(1,6):
    print(i)

# loop In reverse
    # for do reverse in loop we have to take step in negative
for i in range(20,0,-1):
    print(i)  
# printing table of 5 
for i in range(5,51,5):
    print(i) 

#printing table of n

n=int(input("Print the table of ? "))

for i in range(n,(n*10)+1,n):
    print(i) 
    

# loops for string

"""      Loops for strings work slightly differently. You can iterate 
through a string in two ways
 a) Using index values
 b) Iterating directly over the string
"""  
#  a) Using index values

a="Himanshu"
for i in range(len(a)):   #len(a) lenght of string
    print(a[i])

# b) Iterating directly over the string

for i in a:
    print(i)



## Break, continue ,else

"""
     The break statement in Python is used to exit a loop 
prematurely when a certain condition is met. Once break is 
encountered, the loop stops immediately, and control moves 
to the next statement after the loop

    The Continue statement skips one of the iteration and rest of 
the iterations will run for understanding lets say you will not 
run the 16th lap but all other lap will be there

 You have seen the else statement used with if, but it can also 
be used with loops. When else is used with a loop, it only 
executes if the loop completes without encountering a break 
statement. If break is executed, the else block will not run.

"""

for i in range(1,21):
    if i==15:
        break
    else:
        print(i)

# While loop
# 
"""
    The while loop repeats a block of code as long as a condition 
is True. It is useful when the number of iterations is unknown 
before execution

syntax:

while condition:
// code to execute
"""     