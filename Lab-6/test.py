def max_sub_array(arr, low, high):  # top level: (arr,0,7)
    if low == high:  # 说明只含有一个元素,返回
        return arr[low]
    else:
        mid = (low + high) // 2
        S1 = max_sub_array(arr, low, mid)
        S2 = max_sub_array(arr, mid + 1, high)
        S3 = crossing_sub_array(arr, low, mid, high)
        Smax = max(S1, S2, S3)
        return Smax


# 计算S3 分为两部分
# 第一部分为包含mid位置的元素，依次向前遍历找最大的子数组为Sleft
# 第二部分为包含mid+1位置的元素，依次向后遍历，找到最大子数组
# S3就是包含mid和mid+1位置的最大子数组，即为Sleft和Sright的和。
def crossing_sub_array(arr, low, mid, high):
    # 计算左边
    Sleft = -999
    sum = 0
    for i in range(mid, low, -1):
        sum += arr[i]
        Sleft = max(Sleft, sum)

    # 计算右边
    Sright = -999
    sum = 0
    for j in range(mid+1, high+1):
        sum += arr[j]
        Sright = max(Sright, sum)

    S3 = Sleft + Sright
    return S3


arr = [0, 1, 2, 3, 4, -3, 8, 9]
n = len(arr)  # 8
print(max_sub_array(arr, 0, n - 1))
