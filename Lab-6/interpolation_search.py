def interpolation_search(n, S, x):
    low = 0
    high = n - 1
    i = 0

    if S[low] <= x <= S[high]:
        while low <= high and i == 0:
            denominator = S[high] - S[low]
            if denominator == 0:
                mid = low
            else:
                mid = low + int((x - S[low]) * (high - low) // denominator)
            if x == S[mid]:
                i = mid
                return i
            elif x < S[mid]:
                high = mid - 1
            else:
                low = mid + 1
    return -1


S = [1, 2, 3, 4, 5, 6, 7, 8, 9, 100]
n = len(S)

key = int(input('Enter the key value to search:'))

output = interpolation_search(n, S, key)

if output != -1:
    print('Element found at location(started from 0): ', str(output))
else:
    print('Element is not found')
