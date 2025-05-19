"""

Lists are used to store multiple items in a single variable.
"""

# syntax of list , listname[12,09,]

a=[12,13,4,6,"Himanshu",6.7] 

"""
List Items:

List items are ordered, changeable,
 and allow duplicate values. and can be any data types

List items are indexed, the first item has index [0], 
 the second item has index [1] etc
"""

list=[12,"Himanshu",29]
print(list[0]) # 1st index
print(list[1]) # 2nd index
print(list[2])  #3rd index

# To determine how many items a list has, use the len() function:
print(len(list))

# From Python's perspective, lists are defined as objects with the data type 'list':

print(type(list))




# List travesing and methods

# 1st way using index

for i in range(len(list)):
    print(list[i])

# 1st way directly on value

for i in list:
    print(i)



#list methods    

"""
Method	 |   Description
----------|----------------
append()	Adds an element at the end of the list
clear()	    Removes all the elements from the list
copy()	     Returns a copy of the list
count()	     Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	     Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	     Removes the element at the specified position
remove()	Removes the first item with the specified value
reverse()	Reverses the order of the list
sort()	     Sorts the list

"""

ls=[1,2,3,4,5,6]

#adding 7
ls.append(7)
ls.insert(5,69)
print(ls)

ls[0]=100
print(ls)