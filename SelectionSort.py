# selection sort.Exercises2.2-2
__author__ = 'ShiYujin'
__date__ = '2015.5.24'


def SelectionSort(A):
    a = A[:]
    for i in range(0, a.__len__() - 1):
        key = a[i]
        pos = i
        for j in range(i, a.__len__()):
            if a[j] < key:
                key = a[j]
                pos = j
        a[pos] = a[i]
        a[i] = key
    return a

# now let's have a try
a = [31, 41, 59, 26, 41, 58]
a = SelectionSort(a)
for i in a:
    print(i)

