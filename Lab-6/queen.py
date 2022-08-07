# n-Queen problem


def queens(i):
    global count

    if promising(i):
        if i == n:  # last queen
            print("This is the solution " + str(count) + ": ", end="")
            print(col)  # array col start from 0 (root to leaf)
            count += 1
        else:
            for j in range(1, n + 1):
                col[i + 1] = j
                queens(i + 1)


def promising(i):
    k = 1
    flag = True

    while k < i and flag:  # check current queen(i) with all the queens before i-th row
        if col[i] == col[k] or abs(col[i] - col[k]) == i - k:  # not in same column or diagonal
            flag = False  # dead end
        k += 1

    return flag


count = 1
n = 4
# n = 8
col = [0] * (n + 1)
queens(0)  # root
