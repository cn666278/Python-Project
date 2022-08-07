# Quick Select
import numpy as np

def selection(low, high, k):
    pivotPtr = S[low]
    if low == high:
        return S[low]
    else:
        partition(low, high, pivotPtr)
        if k == pivotPtr:
            return S[pivotPtr]
        elif k < pivotPtr:
            return selection(low, pivotPtr - 1, k)
        else:
            return selection(pivotPtr + 1, high, k)
    return -1

def partition(low, high, pivotPtr):
    pivot = S[low]
    j = low

    for i in range(low + 1, high + 1):
        if S[i] < pivot:
            j += 1
            S[i], S[j] = S[j], S[i]

    pivotPtr = j
    S[low], S[pivotPtr] = S[pivotPtr], S[low]


S = [1, 3, 6, 9, 2, 8, 7, 22, 4]
np.random.shuffle(S) # randomize the array
# print(S)
k = int(input("Enter the k for kth-smallest key(k is indexed from 0): "))
print(selection(0, len(S) - 1, k))
