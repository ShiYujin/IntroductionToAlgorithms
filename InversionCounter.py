# Count Invertions. By modify merge sort. With time complexity O(nlgn)
# Problems 2-4
__author__ = 'Administrator'
__date__ = '2015.5.25'


def icounter(A, p, q, r, n):
    import copy
    L = copy.deepcopy(A[p:q])
    R = copy.deepcopy(A[q:r])
    L.append(float("inf"))      # sentinel
    R.append(float("inf"))
    i = 0
    j = 0
    l = L.__len__() - 1
    for k in range(p, r):
        if L[i] <= R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1
            n = n + l - i
    return n


def ICounter(A, p, r, n):
    if p < r - 1:
        q = (p + r) / 2
        n = ICounter(A, p, q, n)
        n = ICounter(A, q, r, n)
        return icounter(A, p, q, r, n)
    return n


def InversionCounter(A):
    a = A[:]
    return ICounter(a, 0, a.__len__(), 0)


# test
x = [4, 3, 2, 1, 0, 8]
print(InversionCounter(x))
