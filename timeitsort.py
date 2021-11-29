import timeit
import random
import quicksort
import sys
sys.setrecursionlimit(9999999)


A = [random.randint(0, 100) for x in range(1000)]
p = 0
r = len(A) - 1
count = 1


def heapsort_f(A, count):
    heap = f"""import heapsort
heap = heapsort.Heapsort().heapsort({A})
"""
    heapsort_time = timeit.Timer(heap).timeit(count)
    print("Heapsort", heapsort_time*1000)


def quicksort_f(A, p, r, count):
    quick = f"""import quicksort
quick = quicksort.Quicksort().quicksort({A}, {p}, {r})
"""
    quicksort_time = timeit.Timer(quick).timeit(count)
    print("Quicksort", quicksort_time*1000)


def countingsort_f(A, count):
    counting = f"""import countingsort
bubble = countingsort.Countingsort().countingsort({A})
"""
    counting_time = timeit.Timer(counting).timeit(count)
    print("Countingsort", counting_time*1000)    


def mergesort_f(A, count):
    merge = f"""import mergesort
merge = mergesort.Mergesort().mergesort({A})
"""
    merge_time = timeit.Timer(merge).timeit(count)
    print("Mergesort", merge_time*1000)     



print("- random list")
heapsort_f(A, count)
quicksort_f(A, p, r, count)
countingsort_f(A, count)
mergesort_f(A, count)
print()


print("- list sorted in ascending order")
A = quicksort.Quicksort().quicksort(A, p, r)
heapsort_f(A, count)
quicksort_f(A, p, r, count)
countingsort_f(A, count)
mergesort_f(A, count)
print()


print("- list sorted in descending order")
A = A[::-1]
heapsort_f(A, count)
quicksort_f(A, p, r, count)
countingsort_f(A, count)
mergesort_f(A, count)
print()

