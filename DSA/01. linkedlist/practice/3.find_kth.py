"""
def find_kth_from_end(list, k):
    slow = list.head
    fast = list.head
    
    while fast.next is not None:
        slow = slow.next
        for i in range (k+1):
            fast=fast.next
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True


def find_kth_from_end(list, k):
    """
    time complexity: O(n)
    space complexity: O(1)
    """
    slow = list.head
    fast = list.head

    # Move fast k steps ahead to create a gap of k nodes between slow and fast
    for _ in range(k):
        if not fast:
            return None
        fast = fast.next

    # Move both pointers until fast reaches the end
    while fast:
        slow = slow.next
        fast = fast.next
    return slow


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = find_kth_from_end(my_linked_list, k)

print(result.value)  # Output: 4


"""
    EXPECTED OUTPUT:
    ----------------
    4
    
"""
