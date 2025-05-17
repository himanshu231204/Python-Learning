# What are operators ? 

# Operators are symbols that perform operations on variables and values. Python has several types of operators for 
#different tasks like arithmetic, comparison, logical operations, and more

# 1) Arithmetic operators
"""
     additiona +
     subtraction -
     multiplication *
     dividions /
     floor divisions //
     modulus %
     exponential **

"""

a=2
b=3
print(a+b)
print(a-b)
print(a*b)
print(a%b)
print(a**b)
print(a//b)
print(a/b)

# 2) Assignment operator
#     A basic assignment operator is simple =


# 3)  Compound assignment Operators

#   Compound assignment operator combines arithmetic operations with 
# using compound assignment operators the reassigning work better

"""
         += -> add and assign
         -= -> sub and assign
         *= -> multiply and assign
         /= -> divides and assign
         //= -> floor divides and assign
         %= -> modulus and assign
         **= -> exponential and assign
"""

c=10
c=c+20
c=c+30

# using compound assignment operator
d=2
d+=10
d+=30
print(c)
print(d)


#   4)  Comparison operator
#        it is also called relational operators, are used to compare two values
#    It always provides boolean results that is True and False
#     Comparison operator are as follows
"""
             ==  -> equal to
             !=  -> not equal to
             >  -> greater than
             <   -> less than
             >=  -> greater than or equal to
             <=  -> less than or equal to


"""
# Comparison operators will work with numbers but you can use them with strings as well.
#  Strings will be comparing the Ascii values of string.

print(a>=b)
print(b!=d)
print(c==d)
print(3>4)



#     5)  Logical Operators

#       Logical operators in Python are used to combine multiple conditions and return a Boolean result (True or False)
"""
          There are 3 types of logical operator

          and -->  Return True if both condition are True
          or --->    Return True if at least one condition is True
          not -->    Reverse the boolean value

"""


print(a>b and b<c)
print(a>c or b<d)
print( not(c>b and  c>d ))
