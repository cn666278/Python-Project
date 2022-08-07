# partition problem
# when we choose w1,w3,w4, it means that the rest are w2,w5, hence the answer only has one:[w1,w3,w4]

def partition(i, weight, remain):
    global w
    global n
    global W
    global include

    if promising(i, weight, remain):
        if weight == W:
            print(include)
        else:
            include[i + 1] = "yes"
            partition(i + 1, weight + w[i + 1], remain - w[i + 1])
            include[i + 1] = "no"
            partition(i + 1, weight, remain - w[i + 1])

def promising(i, weight, remain):
    return weight + remain >= W and (weight == W or weight + w[i + 1] <= W)


w = [1, 6, 4, 3, 2]
n = len(w)
include = ['no'] * n
remain = sum(w)
W = remain / 2
partition(-1, 0, remain)
