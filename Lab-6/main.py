

def chained_mat_mult(n, d):
    # 初始化,矩阵长度为n
    M = [[0 for i in range(n)] for j in range(n)]
    P = [[0 for i in range(n)] for j in range(n)]

    # 矩阵起点为0，但我们只利用起点1
    # for i in range(1, n+1):
    #     M[i][i] = 0

    # range of diagonal: (1, n-1)
    for diagonal in range(1, n):
        # i in range(1, n-d-1)  !!!因为矩阵长度为n,而实际使用的只有n-1
        for i in range(1, n-diagonal):
            j = i + diagonal

            # i <= k <= j-1
            for k in range(i, j):
                # k == i means the initial value of each diagonal
                if k == i:
                    M[i][j] = M[i][k] + M[k+1][j] + d[i-1] * d[k] * d[j]
                    P[i][j] = k

                minM = M[i][k] + M[k+1][j] + d[i-1] * d[k] * d[j]
                if minM < M[i][j]:
                    M[i][j] = minM
                    P[i][j] = k   # record the order of matrix multiplication

    return M, P

def order(P, i, j):
    if i == j:
        print('A' + str(i), end='')
    else:
        k = P[i][j]
        print('(', end='')
        order(P, i, k)
        order(P, k+1, j)
        print(')', end='')


# d = [3, 5, 6, 7, 4, 8, 9]
d = [2, 3, 7, 9, 5 ,2 ,4]

M, P = chained_mat_mult(len(d), d)
print("\nThe optimal matrix order is:")
order(P, 1, len(d)-1)   # max = n-1(started from 1)
print("\n\nThe optimal Matrix multiplication is:" + str(M[1][len(d)-1]))

print("\nMatrix M is:")
# matrix column 0 is not used
for i in range(1, len(d)):
    print("[", end='')
    for j in range(1, len(d)):
        print(str(M[i][j]) + '\t', end='')
    print("]\n")



"""
# 仅用于打印数值表，所以 n <= k
def bin_coef_dp(n, k):
    B = [[0 for i in range(n+1)] for j in range(k+1)]

    for i in range(0, n+1):
        for j in range(0, min(i, k)+1):
            # k = 0 or k = n
            if j == 0 and j == i:
                B[i][j] = 1
            else:
                B[i][j] = B[i-1][j-1] + B[i-1][j]  # 0 < j < i      (0 < k < n)

    return B

n = 3
k = 3
B = bin_coef_dp(n, k)   # 输出数值表到B
print(B[3][2])          # 求值
print(B)
"""