class Heapsort():

    def heapsort(self, A):
        heap_size = len(A)
        self.build_max_heap(A, heap_size)
        for i in range(len(A)-1, 0, -1):
            A[0], A[i] = A[i], A[0]
            heap_size -= 1
            self.max_heapify(A, 0, heap_size)

        return A
    
 
    def build_max_heap(self, A, heap_size):
        for i in range(len(A)//2 - 1, -1, -1):
            self.max_heapify(A, i, heap_size)


    def max_heapify(self, A, i, heap_size):
        largest = i
        l = 2*i + 1
        r = 2*i + 2

        if l < heap_size and A[i] < A[l]:
            largest = l

        else:
            largest = i

        if r < heap_size and A[largest] < A[r]:
            largest = r

        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            self.max_heapify(A, largest, heap_size)

