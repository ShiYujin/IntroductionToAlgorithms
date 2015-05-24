# insertion sort.chapter2.1
__author__ = 'ShiYujin'
__date__ = '2015.5.24'


def InsertionSort(A):
    a = A[:]
    for i in range(1, a.__len__()):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a

# now let's have a try
a = [31, 41, 59, 26, 41, 58]
a = InsertionSort(a)
for i in a:
    print(i)
