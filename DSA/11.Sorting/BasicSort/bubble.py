"""
Bubble Sort
- 서로 인접한 두 원소를 검사하여 정렬하는 알고리즘
- Compare the first and second element, if the first is greater than the second, swap them.
- Repeat the process for the entire list.
- 'bubble up the largest element to the end of the list'
- Time Complexity: O(n^2)
- Space Complexity: O(1)
"""


def bubble_sort(my_list):
    for i in range(len(my_list) - 1, 0, -1):
        for j in range(i):
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
    return my_list


print(bubble_sort([4, 2, 6, 5, 1, 3]))


"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
 """
