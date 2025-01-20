"""
implement a stack using a linked list
stack use top as 
"""


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Stack:
    def __init__(self, value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1  # instead of length

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next


my_stack = Stack(4)
my_stack.print_stack()
