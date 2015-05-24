__author__ = 'ShiYujin'
__date__ = '2015.5.24'
def InsertionSort(A):
    for i in range(1, A.__len__()):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key
    return A

a = [5, 2, 4, 6, 1, 3]
a = InsertionSort(a)
for i in a:
    print(i)
