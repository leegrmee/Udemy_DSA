"""
/first attempt/

def find_middle_node(self):
        temp = self.head
        slow_p = temp.next
        fast_p = temp.next.next
        while fast_p is not None and fast_p.next is not None:
            temp = slow_p
            slow_p =temp.next
            fast_p = fast_.next.next
        return temp
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

    def find_middle_node(self):
        """
        time complexity: O(n)
        space complexity: O(1)
        """
        slow_p = self.head
        fast_p = self.head
        while fast_p is not None and fast_p.next is not None:
            slow_p = slow_p.next
            fast_p = fast_p.next.next

        return slow_p


my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)

print(my_linked_list.find_middle_node().value)


"""
    EXPECTED OUTPUT:
    ----------------
    3
    
"""
