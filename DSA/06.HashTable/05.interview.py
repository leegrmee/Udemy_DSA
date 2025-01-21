def item_in_common(list1, list2):
    for i in list1:
        for j in list2:
            if i == j:
                return True
    return False


"""
In this approach, the time complexity is O(n^2)
becuase it uses nested loop.
"""


def item_in_common(list1, list2):
    my_dict = {}
    for i in list1:
        my_dict[i] = True
    for j in list2:
        if j in my_dict:
            return True
    return False


"""
In this approach, the time complexity is O(n)
We had go through the each list once, which we could say 
that is O of 2n, but we can drop the constant, so it is O(n)
"""


list1 = [1, 3, 5]
list2 = [2, 4, 5]

print(item_in_common(list1, list2))
