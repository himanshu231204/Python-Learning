"""
Tuple
Tuples are used to store multiple items in a single variable.

Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage.

A tuple is a collection which is ordered and unchangeable.

Tuples are written with round brackets.


Note:

1) Tuple items can be of any data type:
    A tuple can contain different data types:

2) To determine how many items a tuple has, use the len() function:

3) Since tuples are indexed, they can have items with the same value:

4) Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

5) When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

6) Tuple items are ordered, unchangeable, and allow duplicate values.

Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

"""
#syntax
tuple=(1,2,20)
print(len(tuple))

#tuple is traverse as same sa list

# List travesing and methods

# 1st way using index

for i in range(len(tuple)):
    print(tuple[i])

# 1st way directly on value

for i in tuple:
    print(i)

    #