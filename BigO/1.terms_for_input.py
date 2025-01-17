def print_items(a, b):
    for i in range(a):
        print(i)

    for j in range(b):
        print(j)


print_items(1, 10)

"""
When the fucntion has two different parameters, you cannot simplify this all the way 
down to one variable and call it O of n.
In this case, time complexity is O of a + b
"""


def print_items(a, b):
    for i in range(a):
        for j in range(b):
            print(i, j)


print_items(1, 10)

"""
Similary, if you have a nested loop, you cannot simplify this all the way down to one variable and call it O of n.
In this case, time complexity is O of a times b
"""
