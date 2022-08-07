# Quick Sort
import numpy as np

def quicksort(low, high, S):
    #     pivotPtr = S[low]
    if (high > low):
        pivotPtr = partition(low, high, S)
        quicksort(low, pivotPtr - 1, S)
        quicksort(pivotPtr + 1, high, S)
    return S


def partition(low, high, S):
    i = low + 1
    j = high
    pivot = S[low]

    while True:  # scan left and right, check whether scan is over and exchange the elements
        while S[i] < pivot: # 当S[i] < pivot, let i++
            i += 1
            if i == high:
                break
        while pivot < S[j]:
            j -= 1
            if j == low:
                break
        if i >= j:
            break
        S[i], S[j] = S[j], S[i]  # exchange S[j] and S[i] so that all element on left side of i is less than pivot

    S[low], S[j] = S[j], S[low] # 指针相遇时交换S[low] 和 S[j]
    return j


S = [1, 3, 6, 9, 2, 8, 3, 22, 4]
print(quicksort(0, len(S) - 1, S))
