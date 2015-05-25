# Merge sort.chapter2.3.1
__author__ = 'ShiYujin'
__date__ = '2015.5.24'


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


def MSort(A, p, r):
    if p < r - 1:
        q = (p + r) / 2
        MSort(A, p, q)
        MSort(A, q, r)
        merge(A, p, q, r)
    return A


def MergeSort(A):
    a = A[:]
    return MSort(a, 0, a.__len__())

# little test
a = [6, 5, 4, 3, 2, 1, 0]
a = MergeSort(a)
for i in a:
    print(i)