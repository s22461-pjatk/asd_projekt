class Countingsort():

    def countingsort(self, A):
        maximum = 0
        for i in range(len(A)):
            if A[i] > maximum:
                maximum = A[i]

        buckets = [0] * (maximum + 1)

        for i in A:
            buckets[i] += 1

        i = 0
        for j in range(maximum+1):
            for a in range(buckets[j]):
                A[i] = j
                i += 1

        return A