def swap(my_list, index1, index2):
    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp


def pivot(my_list, pivot_index, end_index):
    """
    Rearrange the list so that all the elements less than the pivot are on the left and all the elements greater than the pivot are on the right.
    Return the index of the pivot element.
    """
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(
        my_list, pivot_index, swap_index
    )  # For the last swap that puts the pivot in the middle
    return swap_index


def quicksort_helper(my_list, left, right):
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quicksort_helper(my_list, left, pivot_index - 1)
        quicksort_helper(my_list, pivot_index + 1, right)
    return my_list


def quicksort(my_list):
    return quicksort_helper(my_list, 0, len(my_list) - 1)


my_list = [4, 6, 1, 7, 3, 2, 5]
print(quicksort(my_list))
print(my_list)
