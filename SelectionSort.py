# selection sort.Exercises2.2-2
__author__ = 'ShiYujin'
__date__ = '2015.5.24'


def SelectionSort(A):
    for i in range(0, A.__len__() - 1):
        key = A[i]
        pos = i
        for j in range(i, A.__len__()):
            if A[j] < key:
                key = A[j]
                pos = j
        A[pos] = A[i]
        A[i] = key
    return A

# now let's have a try
a = [31, 41, 59, 26, 41, 58]
a = SelectionSort(a)
for i in a:
    print(i)
