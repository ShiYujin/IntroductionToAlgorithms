# insertion sort
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

# now let's have a try
a = [31, 41, 59, 26, 41, 58]
a = InsertionSort(a)
for i in a:
    print(i)
