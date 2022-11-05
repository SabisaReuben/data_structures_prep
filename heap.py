# A binary heap is a data structure that hold heap tree propery i.e
# parent nodes are greater than the leaf nodes.

# Often, this data structure is implemented using an array.
# These module implements this data structure using an array and 
# supports all basic operation such as insertion, deletion and sorting

from array import array
import math
class Heap:
    __slots__ = ("_heap","_count")
    def __init__(self,iterable, maxsize =100):
        """
        : iterable: initial elements of the array
        : maxsize: the maximum number of elements heap can hold
        """
        self._count = len(iterable);
        self._heap = array('i',iterable)


    def height(self):
        """
        : return: the height of the heap tree
        """
        return math.floor(math.log(self._count,2))


    def size(self):
        """
        : return: the total number of items in the heap
        """
        return self._count


    def heapify(self, n, largest):
        """
        The method build a heap after insertion or deletion.
        The method adobts trickle up approach where leaf nodes are compared
        parent nodes and swapped until heap property is established. 
        : n: the index of the end element: presumably the the size of the array
        : largest: then index of the current largest element
        """

        l = largest

        #given the heap index starts from 0, the leafs of the node at index i
        # can be est in the following eq
        # p = i left = 2 * i +1, right = 2 * i +2 otherwise if index started at
        # 1, then left could be 2 * i
        
        left, right = 2 * largest + 1, 2 * largest + 2

        if left < n and self._heap[left] > self._heap[l]:
            l = left

        if right < n and self._heap[right] > self._heap[l]:
            l = right

        # swap the element if the index changed

        if l != largest:
            self._heap[l], self._heap[largest] = self._heap[largest], self._heap[l]
            self.heapify(n, l)

    def build_heap(self):
        parents = self.size() // 2 -1

        for i in range(parents, -1, -1):
            self.heapify(self.size(), i)


    def heap_sort(self):
        parents = self.size() // 2 -1
        self.build_heap()

        for i in range(self.size()-1, -1, -1):
            print(self._heap[0], end = " => ")
            self._heap[0], self._heap[i] = self._heap[i], self._heap[0]
            self.heapify(i, 0)

    def insert(self, value):
        self._heap.extend(value)
        self._count +=1






