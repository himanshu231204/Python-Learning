#Dictionary
#Dictionaries are used to store data values in key:value pairs.

#A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

#Syntax
#dis={key:value}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#--------------------------------------

"""
Dictionary Items
Dictionary items are ordered, changeable, and do not allow duplicates.

Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

"""
thisdict2 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict2["brand"])

#===================================================

"""
Ordered or Unordered?
As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.

-------------
Changeable
Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

"""
#----------------------
"""
Duplicates Not Allowed
Dictionaries cannot have two items with the same key:
"""
thisdict4= {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict4)

#===========================

"""
Dictionary Items - Data Types
The values in dictionary items can be of any data type:
"""
thisdict5 = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}

#===========================================

"""
Accessing Items:

You can access the items of a dictionary by 
referring to its key name, inside square brackets:
"""
thisdict6 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict6["model"]

#There is also a method called get() that will give you the same result:
x = thisdict6.get("model")

#Get Keys
#The keys() method will return a list of all the keys in the dictionary.
x = thisdict6.keys()

#Get Values
#The values() method will return a list of all the values in the dictionary.
x = thisdict6.values()


#-----------------------------===================

"""
Loop Through a Dictionary
You can loop through a dictionary by using a for loop.

When looping through a dictionary, the return value are the keys 
of the dictionary, but there are methods to return the values as well.
"""
#Print all key names in the dictionary, one by one:
for x in thisdict:
  print(x)

#Print all values in the dictionary, one by one
for x in thisdict:
  print(thisdict[x])  

  #------------------------------------------------------

  """
  Dictionary Methods
Python has a set of built-in methods that you can use on dictionaries.

Method	    Description
clear()	     Removes all the elements from the dictionary
copy()	      Returns a copy of the dictionary
fromkeys()	  Returns a dictionary with the specified keys and value
get()	       Returns the value of the specified key
items()	        Returns a list containing a tuple for each key value pair
keys()	        Returns a list containing the dictionary's keys
pop()	        Removes the element with the specified key
popitem()	     Removes the last inserted key-value pair
setdefault()	Returns the value of the specified key. If the key does not exist: insert the key, with the specified value
update()	   Updates the dictionary with the specified key-value pairs
values()	   Returns a list of all the values in the dictionary
  
  """

  #=======================================

  """
  Copy a Dictionary
You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2.

There are ways to make a copy, one way is to use the built-in Dictionary method copy().
  """

thisdict9 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1
}
mydict = thisdict9.copy()
print(mydict)  

#================================================================

"""
Nested Dictionaries:

A dictionary can contain dictionaries, 
this is called nested dictionaries.
"""

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

"""
Access Items in Nested Dictionaries
To access items from a nested dictionary, you use the name of the dictionaries, 
starting with the outer dictionary:
"""
#Print the name of child 2:

print(myfamily["child2"]["name"])

"""
Loop Through Nested Dictionaries
You can loop through a dictionary by 
using the items() method like this:
"""

#Loop through the keys and values of all nested dictionaries:

for x, obj in myfamily.items():
  print(x)

  for y in obj:
    print(y + ':', obj[y])