""""
     Unicode is a universal character encoding standard that 
assigns a unique number (code point) to every character, 
regardless of language

   we can check them by using ord() function in python and 
convert them back using chr() function.

"""
a="A"
print(ord(a))

b=65
print(chr(b))


# String Indexing

"""
         Indexing starts from 0 and 
goes till the number of characters you have.

            There is negative indexing as well and it starts from -1, but 
the starting position is from the back of the strin

"""

c="Himanshu"
print(c[0])
print(c[1])
print(c[2])
print(c[3])
print(c[-1])


# String Slicing

""""            Slicing means cutting out a slice from string and this is also 
done using index values

 eg - a = “hello”  a[1:4:1]  ==> output “ell

 So here we have start , stop and steps position and keep a 
note if we use stop at 4 it will slice till 3 only. 

"""

d="Gym Boy Himanshu"

#how to slice
   # D[start : stop : step positions]
   
print(d[0:3:1])  
print(d[4:8:1])  



# Types Conversion

"""        For understanding type conversion you have to look at these 4 things
            1)  int()
            2) float()
            3) str()
            4) bool()

            There are more functions like this but these are 4 main 
function, looking at these functions you can guess these are 
used to convert one data type to another
"""
#example

e=12
f=0
print(bool(e))
print(bool(f))
print(str(e))
print(complex(e))
print(float(e))

#  Note

"""        There are truthy values and Falsy values, and there are only 
            7 falsy values that means only 7 things will be converted to 
             false rest True.

             1)   0
             2)   0.0
             3)   False
             4)   ""
             5)   []
             6)   {}
             7)   ()

              All these values are falsy remaining will be converted to True.

"""

# Types of Conversions
"""
          There are 2 Types Of Conversions Implicit and Expilicit.

          Implicit:                               
                                             
           In this python automatically
           converts data from one data 
           type to another.
           You have already seen the 
            example before
             e.g-> a=12
                   print (a/2)
                   output - 6.0


            Explicit:
          --------->   
           In this we as a user use in build
           functions to convert one data 
           type to another
              
                               

int() 
 float()                   
complex()            
str()                      
list()                      
tuple()                  
set()                      
dict()                     
bool()                    

"""