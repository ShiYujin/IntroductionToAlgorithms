# Describe a O(nlogn)-time algorithm that, given a set S of n integers and another
# integer x, determines whether or not there exist two elements in S whose sum is
# exactly x.
# Exercise 2.3-7
__author__ = 'ShiYujin'
__date__ = '2015.5.24'


def FindNum(A, x, start, end):
    if start >= end:
        return -1
    pos = (start + end) / 2
    if A[pos] > x:
        return FindNum(A, x, start, pos)
    elif A[pos] < x:
        return FindNum(A, x, pos + 1, end)
    else:
        return pos


def Find(A, x):
    return FindNum(A, x, 0, A.__len__())


def FindAdder(A, sum):
    # import module
    import sys
    sys.path.append('e:\Project\python\IntroductionToAlgorithms')
    import MergeSort
    # sort first
    a = MergeSort.MergeSort(A)
    for i in A:
        adder = sum - i
        if Find(A, adder) != -1:
            return [i, adder]
    return 0

# test
a = [4, 2, 6, 7, 33, 5, 12, 52]
f = FindAdder(a, 35)
for i in f:
    print(i)
