# Sets
myset = {"apple", "banana", "cherry"}

"""
1> Sets are used to store multiple items in a single variable.
2> A set is a collection which is unordered, unchangeable*, and unindexed.
"""
#------------------------------------------------------------------------------------
"""
Set Items:
Set items are unordered, unchangeable, and do not allow duplicate values.

Unordered:
Unordered means that the items in a set do not have a defined order.
Set items can appear in a different order every time you use them, and cannot be referred to by index or key.

Unchangeable:
Set items are unchangeable, meaning that we cannot change the items after the set has been created.

Notes:
Once a set is created, you cannot change its items, but you can remove items and add new items.

Duplicates Not Allowed
Sets cannot have two items with the same value.

Set Items - Data Types
Set items can be of any data type:

"""
#------------------------------------------------------------------

set1 = {"abc", 34, True, 40, "male"}
print(set1)
#-----------------------------------------------------------

"""
Note: The values True and 1 are considered 
the same value in sets, 
and are treated as duplicates:

Note: The values False and 0 are considered the same 
value in sets, and are treated as duplicates:
"""
#--------------------------------------------------------------------

thisset = {"apple", "banana", "cherry", True, 1, 2}

print(thisset)

thisset2 = {"apple", "banana", "cherry", False, True, 0}

print(thisset2)

#-------------------------------------------------------------------


"""
Loop Items
You can loop through the set items by using a for loop:

"""
thisset3 = {"apple", "banana", "cherry"}
for x in thisset3:
  print(x)

#-------------------------------------------------------------------



"""
Set Methods:

Python has a set of built-in methods that you can use on sets.

Method                          Shortcut     Description
add()                                         Adds an element to the set
clear()                                       Removes all the elements from the set
copy()                                        Returns a copy of the set
difference()                    -             Returns a set containing the difference between two or more sets
difference_update()             -=            Removes the items in this set that are also included in another, specified set
discard()                                     Remove the specified item
intersection()                  &             Returns a set, that is the intersection of two other sets
intersection_update()           &=            Removes the items in this set that are not present in other, specified set(s)
isdisjoint()                                   Returns whether two sets have an intersection or not
issubset()                      <=            Returns whether another set contains this set or not
                                <             Returns whether all items in this set are present in another set
issuperset()                    >=            Returns whether this set contains another set or not
                                >             Returns whether all items in other set(s) are present in this set
pop()                                          Removes an element from the set
remove()                                       Removes the specified element
symmetric_difference()          ^             Returns a set with the symmetric differences of two sets
symmetric_difference_update()  ^=            Inserts the symmetric differences from this set and another
union()                         |             Return a set containing the union of sets
update()                        |=            Update the set with the union of this set and others

"""

a={1,2,3,4,5,6,}
b={4,5,6,7,8,9,10}
print(a|b)
print(a&b)
print(a.pop())

