class MaxHeap:
    def __init__(self):
        self.heap = []

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        """
        return the index of the parent node
        """
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1  # index of the last element

        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        # self.heap.pop()은 힙의 마지막 요소를 제거하고 그 값을 반환
        # 그 다음 self.heap[0] = self.heap.pop()은 이 마지막 요소를 힙의 루트(첫 번째 요소)에 할당하여 루트를 제거
        self._sink_down(0)
        return max_value

    """
    마지막 값을 사용하는 이유
    완전 이진 트리 유지

    힙의 삭제 과정에서 빈 공간을 최소화하기 위해: 
    힙의 루트를 제거하면 트리의 완전성을 유지하기 위해 빈 공간이 생기는데, 이 빈 공간을 메우기 위해 
    마지막 요소를 루트로 가져옵니다. 
 
    효율성
    배열에서 마지막 요소를 제거하는 pop() 연산은 O(1)
    이를 루트에 할당하고 싱크다운을 수행하면, 전체 remove 연산의 시간 복잡도는 O(log n)    
    """
