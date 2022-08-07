# sum_of_subsets

def sum_of_subsets(i, weight, remain):
    global w
    global W
    global n
    global include

    if promising(i, weight, remain):
        if weight == W:
            print(include)
        else:
            include[i + 1] = "yes"
            sum_of_subsets(i + 1, weight + w[i + 1], remain - w[i + 1])
            include[i + 1] = "no"
            sum_of_subsets(i + 1, weight, remain - w[i + 1])

def promising(i, weight, remain):
    return (weight + remain >= W) and (weight == W or weight + w[i + 1] <= W)


w = [5, 6, 10, 11, 16]
W = 21
n = len(w)
include = ['no'] * n
remain = sum(w)
sum_of_subsets(-1, 0, remain)