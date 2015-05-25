# Insertion sort on small arrays in merge sort. With O(nk+nlg(n/k)) run time.
# To be better than Merge Sort, k < lgn.
# Problem 2.1
__author__ = 'ShiYujin'
__date__ = '2015.5.25'


def InsertionSort(a, p, r):
    for i in range(p, r):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def merge(A, p, q, r):
    import copy
    L = copy.deepcopy(A[p:q])
    R = copy.deepcopy(A[q:r])
    L.append(float("inf"))      # sentinel
    R.append(float("inf"))
    i = 0
    j = 0
    for k in range(p, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
    return A


def MSort(A, p, r, k):
    if p + k >= r:
        InsertionSort(A, p, r)
    elif p < r - 1:
        q = (p + r) / 2
        MSort(A, p, q, k)
        MSort(A, q, r, k)
        merge(A, p, q, r)
    return A


def InsertionMergeSort(A):
    a = A[:]
    import math
    n = a.__len__()
    k = int(math.log(n, 2))
    MSort(a, 0, n, k)
    return a

# now let's have a try
a = [31, 41, 59, 26, 41, 58, 6, 5, 4, 3, 2, 1]
a = InsertionMergeSort(a)
for i in a:
    print(i)
