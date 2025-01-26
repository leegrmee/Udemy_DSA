"""
Insertion Sort
- 두번째 원소부터 시작
- 왼쪽 원소들과 비교하여 자신의 위치를 찾는 알고리즘
- Start from the second element and compare it with the left elements and find its position.
Big O

- Time Complexity
the worst case is O(n^2) because there are nested loops
But, if the list is aleady sorted or almost sorted, it can be O(n).
For instance, if the list is [1,2,4,3,5], it will be O(n) because it will only go through the inner loop once 
and the it goes linearly.
Only Insertion Sort is O(n) when you start with sorted (or almost sorted) data.

- Space Complexity: O(1)
"""


def insertion_sort(my_list):
    for i in range(1, len(my_list)):
        temp = my_list[i]
        j = i - 1
        while temp < my_list[j] and j > -1:
            my_list[j + 1] = my_list[j]
            my_list[j] = temp
            j -= 1
    return my_list


print(insertion_sort([4, 2, 6, 5, 1, 3]))


"""
    EXPECTED OUTPUT:
    ----------------
    [1, 2, 3, 4, 5, 6]
 """
