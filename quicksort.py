class Quicksort():

    def partition(self, A, p, r):
        x = A[r]
        i = p-1   
        for j in range(p, r):
            if A[j] <= x:
                i += 1
                A[i], A[j] = A[j], A[i]
        A[i+1], A[r] = A[r], A[i+1]
        return i + 1, A

    def quicksort(self, A, p, r):
        if p < r:
            q, A = self.partition(A, p, r)
            A = self.quicksort(A, p, q-1)
            A = self.quicksort(A, q+1, r)
        return A
