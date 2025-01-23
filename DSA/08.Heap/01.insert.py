class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        """
        return the index of the left child node
        """
        return 2 * index + 1

    def _right_child(self, index):
        """
        return the index of the right child node
        """
        return 2 * index + 2

    def _parent(self, index):
        """
        return the index of the parent node
        """
        return (index - 1) // 2

    def _swap(self, index1, index2):
        """
        swap the value of the two nodes
        """
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1  # index of the last element

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)
