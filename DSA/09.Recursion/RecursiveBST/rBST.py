class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while True:
            if new_node.value == temp.value:
                return False
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right

    def contains(self, value):
        """
        method to check whether a certain value exists within the tree
        """
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

    def __r_contains(self, current_node, value):
        if current_node is None:
            return False
        if value == current_node.value:
            return True
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)

    def r_contains(self, value):
        return self.__r_contains(self.root, value)

    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self.__r_insert(self.root, value)

    def min_value(self, current_node):
        """
        To find and return the minimum value in a binary search tree (BST) starting from a given node.
        """
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value

    def __delete_node(self, current_node, value):
        """
        In this method, to delete a node which this method returns means to remove from call stack
        """
        if current_node is None:
            return None
        if value < current_node.value:
            current_node.left = self.__delete_node(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__delete_node(current_node.right, value)
        else:
            if current_node.left is None and current_node.right is None:
                return None
            elif current_node.left is None:
                current_node = current_node.right
            elif current_node.right is None:
                current_node = current_node.left
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min
                current_node.right = self.__delete_node(
                    current_node.right, sub_tree_min
                )
        return current_node

    def delete_node(self, value):
        self.root = self.__delete_node(self.root, value)


my_tree = BinarySearchTree()
my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)

"""
       2
      / \
     1   3
"""

print("root:", my_tree.root.value)
print("root.left =", my_tree.root.left.value)
print("root.right =", my_tree.root.right.value)


my_tree.delete_node(2)

"""
       3
      / \
     1   None
"""


print("\nroot:", my_tree.root.value)
print("root.left =", my_tree.root.left.value)
print("root.right =", my_tree.root.right)


"""
    EXPECTED OUTPUT:
    ----------------
	root: 2
	root.left = 1
	root.right = 3

	root: 3
	root.left = 1
	root.right = None

"""
