# Creating a Function
# In Python a function is defined using the def keyword:

def name():
    print("himanshu")

    #Calling a Function
   # To call a function, use the function name followed by parenthesis:
name()    


#Parameters & arguments
"""
A parameter is the variable 
listed inside the parentheses 
in the function definition.

An argument is the value that is 
sent to the function when it is called.

"""
def sum(a,b):
    print(f"sum of number is {a+b}")
sum(12,3)
sum(9,10)    

## so in above example (a,b) is parametr & (12,3) is arguments

# keywords arguments
"""
You can also send arguments with the key = value syntax.

This way the order of the arguments does not matter.

"""
def bio(name,age):  #name,age is key
    print(f"your name is {name} and your age is {age}")

bio(age=20,name="Himanshu")    

#Default Parameter Value
"""
The following example shows how to use a default parameter value.

If we call the function without argument, it uses the default value:
"""

def my_function(country = "Norway"):
    print("I am from " + country)
                      
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# Arbitrary Arguments, *args

"""
If you do not know how many arguments that will be passed into your function,
 add a * before the parameter name in the function definition.

This way the function will receive a tuple of arguments, 
and can access the items accordingly:

"""
def my_function(*kids):
  print("The youngest child is " + kids[2]) #kids[index of tuples]

my_function("Emil", "Tobias", "Linus")


# Return and print in functions

"""
To let a function return a value,
 use the return statement:
"""
def my_function(x):
  return 5 * x

print(my_function(3))



#The pass Statement
"""
function definitions cannot be empty, 
but if you for some reason have a function
 definition with no content, put in the pass 
 statement to avoid getting an error.
"""
def myfunction():
  pass


#Recursions
"""
Python also accepts function recursion,
which means a defined function can call itself.

"""
def tri_recursion(k):
  if(k > 0):
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results:")
tri_recursion(6)