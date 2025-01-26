"""
Selection Sort
- 가장 작은 원소를 찾아 교환하는 알고리즘
- Find the smallest element in the list and swap it with the first element.
- Repeat the process for the entire list.
- Time Complexity: O(n^2)
- Space Complexity: O(1)
"""


def selection_sort(my_list):
    for i in range(len(my_list) - 1):
        min_index = i
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
        if i != min_index:
            temp = my_list[i]
            my_list[i] = my_list[min_index]
            my_list[min_index] = temp
    return my_list


print(selection_sort([4, 2, 6, 5, 1, 3]))


"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
 """
