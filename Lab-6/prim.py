import numpy as np


def prim(n, W, F):
    global vnear

    for i in range(0, n):
        nearest[i] = 0  # 对于所有顶点(v0-vn)，将v0初始化为Y中的最近顶点
        distance[i] = W[0][i]  # 将与Y的距离初始化为到v0的边上的权重

    for k in range(n - 1):  # 由于连接n个顶点需要n-1条边，将所有n-1个顶点加入Y中
        min = np.inf        # INF
        for i in range(1, n):  # 检查每个顶点(从v1开始）是否与Y最近
            if 0 <= distance[i] < min:
                min = distance[i]
                vnear = i  # vnear is the index of selected vertex to be added(如果后续有更短距离仍会更新vnear)

        # e = edge between two vertices indexed by vnear and nearest[vnear]
        # add e to F
        # [vnear]: 当前距离最短顶点索引
        # [nearest[vnear]]: Y中离v[vnear]距离最短顶点索引
        # W[vnear][nearest[vnear]]: Y中离v[vnear]距离最短顶点与v[vnear]之间的边
        F.append(W[vnear][nearest[vnear]])
        distance[vnear] = -1  # 将以 vnear 为索引的顶点加入Y中(负数表示line 14-16里不再添加）
        Y.append(vnear)

        for i in range(0, n):
            if W[i][vnear] < distance[i]:  # 对于每个不在Y中的顶点，更新它与Y(新添加顶点)的值
                distance[i] = W[i][vnear]
                nearest[i] = vnear
    return F,Y


_ = np.inf
W = [  # the graph
    [0, 1, 3, _, _],  # 0代表该顶点（v0）, 1代表顶点v0-v1的距离 ...
    [1, 0, 3, 6, _],  # 0代表该顶点（v1）
    [3, 3, 0, 4, 2],
    [_, 6, 4, 0, 5],
    [_, _, 2, 5, 0],
]

Y = [0]  # selected vertices,开始时 Y={v0}
F = []  # selected edges
n = len(W[0])  # n>=2

# 空数组不能直接指定位置!!! list[0]
nearest = [0] * n  # Y中与vi最接近的顶点的索引
distance = [0] * n  # 一条边的权重，该边位于 vi 与索引为 nearest[i] 的顶点之间

F,Y = prim(n, W, F)
print(F)
print(Y)


