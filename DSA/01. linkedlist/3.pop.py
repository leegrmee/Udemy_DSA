class Node:

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:

    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

        return True

    def pop(self):
        """
        A method that removes the last node from the linked list and returns it.
        """

        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp

        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    """
    pre = self.tail
    pre.next = None 
    이렇게 작성할 경우
    현재 tail을 pre에 할당하려고 합니다
    이는 잘못된 방식입니다. 왜냐하면:
    pre는 이미 마지막 노드의 이전 노드를 가리키고 있는데
    현재 tail을 pre에 할당하면 원래 가지고 있던 이전 노드에 대한 참조를 잃어
    """


my_linked_list = LinkedList(1)
my_linked_list.append(2)

# (2) Items - Returns 2 Node
print(my_linked_list.pop().value)
# (1) Item -  Returns 1 Node
print(my_linked_list.pop().value)
# (0) Items - Returns None
print(my_linked_list.pop())
