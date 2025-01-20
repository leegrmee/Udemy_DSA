"""
The Node class will represent an individual node within the linked list, 
while the LinkedList class will manage the overall list structure.
"""


class Node:

    def __init__(self, value):
        """
        A constructor that takes a value as an argument and initializes the value attribute of the node.
        A next attribute, initialized to None, which will store a reference to the next node in the list.
        """
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, value):
        """
        A constructor that takes a value as an argument,
        creates a new Node with that value,
        and initializes the head and tail attributes of the linked list to point to the new node.
        A length attribute, initialized to 1,
        which represents the current number of nodes in the list.
        """
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        """
        A method that prints the entire linked list from the head to the tail.
        """
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_linked_list = LinkedList(4)

print("Head:", my_linked_list.head.value)
print("Tail:", my_linked_list.tail.value)
print("Length:", my_linked_list.length)


"""
    EXPECTED OUTPUT:
    ----------------
    Head: 4
    Tail: 4
    Length: 1
    
"""
