class ArrayTest:
    def __init__(self, initial_capacity=16):
        # Ensure capacity is a power of 2 and at least 16
        capacity = max(16, 1 << (initial_capacity - 1).bit_length())
        self._array = [0] * capacity
        self._size = 0
        self._capacity = capacity

    def _resize(self, new_capacity):
        new_array = [0] * new_capacity
        for i in range(self._size):
            new_array[i] = self._array[i]
        self._array = new_array
        self._capacity = new_capacity

    def size(self):
        return self._size

    #     count = 0
    #     for item in self._array:
    #         if item != 0:  # assuming 0 represents empty slot
    #             count += 1
    #     return count

    # In this case time complexity is O on N , because it's necessary to check through array
    # Also, in this case, if array has 0 as an element, it can occur error

    def capacity(self):
        return self._capacity

    def is_empty(self):
        return self._size == 0

    def at(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")
        return self._array[index]

    def push(self, item):
        if self._size == self._capacity:
            self._resize(self._capacity * 2)
        self._array[self._size] = item
        self._size += 1

    def insert(self, index, item):
        if index < 0 or index > self._size:
            raise IndexError("Index out of bounds")

        if self._size == self._capacity:
            self._resize(self._capacity * 2)

        # Shift elements to the right
        for i in range(self._size, index, -1):
            self._array[i] = self._array[i - 1]

        self._array[index] = item
        self._size += 1

    def prepend(self, item):
        self.insert(0, item)

    def pop(self):
        if self.is_empty():
            return None

        item = self._array[self._size - 1]
        self._size -= 1

        # Resize if size is 1/4 of capacity
        if self._size <= self._capacity // 4 and self._capacity > 16:
            self._resize(self._capacity // 2)

        return item

    def delete(self, index):
        if index < 0 or index >= self._size:
            raise IndexError("Index out of bounds")

        # Shift elements to the left
        for i in range(index, self._size - 1):
            self._array[i] = self._array[i + 1]

        self._size -= 1

        # Resize if size is 1/4 of capacity
        if self._size <= self._capacity // 4 and self._capacity > 16:
            self._resize(self._capacity // 2)

    def remove(self, item):
        # Find all indices with the item
        indices = []
        for i in range(self._size):
            if self._array[i] == item:
                indices.append(i)

        # Delete from the end to avoid index shifting issues
        for i in reversed(indices):
            self.delete(i)

        return len(indices) > 0

    def find(self, item):
        for i in range(self._size):
            if self._array[i] == item:
                return i
        return -1


def main():
    ar = ArrayTest()


if __name__ == "__main__":
    main()
