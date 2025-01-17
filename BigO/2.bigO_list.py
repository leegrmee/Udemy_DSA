# Big O of list
"""
*Big O measures worst case*

[11,3,34,7]

Appending to a list (.appned)and 
Removing last element(.pop) from a list no needs reindexing
and the time complexity is O of 1 


Removing an element from (.pop(0))
Inserting an element into a list 
becuase of the re-indexing that has to happen, 
the time complexity is O of n


Inserting an element in the middle is O of n

Searching for an element in a list is O of n
But, if you look for an element by its index, 
you can go directly to that place in memory based on that index,
so the time complexity is O of 1
"""
