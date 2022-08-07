import numpy as np


def dijkstra(n, W, F):
    global vnear

    for i in range(0, n):
        touch[i] = 0            # 对于所有顶点(v0-vn)，将v0初始化为始于v0的当前最短路径上的最后一个顶点
        length[i] = W[0][i]     # 并将该路径的长度初始化为始于v0的边的长度

    for k in range(n - 1):  # 将所有n-1个顶点加入Y中
        min = np.inf  # INF
        for i in range(1, n):  # 检查每个(从v1开始）拥有最短路径的顶点
            if 0 <= length[i] < min:
                min = length[i]
                vnear = i  # vnear is the index of selected vertex to be added

        # e = edge of vertices that start from index touch[vnear] to vnear.
        # add e to F
        F.append(W[touch[vnear]][vnear])

        for i in range(0, n):
            if length[vnear] + W[vnear][i] < length[i]:  # 对于每个不在Y中的顶点，更新它到v0的最短路径
                length[i] = length[vnear] + W[vnear][i]
                touch[i] = vnear
        length[vnear] = -1  # 将以 vnear 为索引的顶点加入Y中
    return F


_ = np.inf
W = [  # the graph
    [0, 7, 4, 6, 1],  # 0代表该顶点（v0）, 1代表顶点v0-v1的距离 ...
    [_, 0, _, _, _],  # 0代表该顶点（v1）
    [_, 2, 0, 5, _],
    [_, 3, _, 0, _],
    [_, _, _, 1, 0],
]

Y = []  # selected vertices,开始时 Y={v0}
F = []  # selected edges
n = len(W[0])  # n>=2

# 空数组不能直接指定位置!!! list[0]
touch = [0] * n  # Y中顶点v的索引，在仅以Y中顶点为中间顶点时，边<v0,vi>是从v0-vi的当前最短路径上的最后一条边
length = [0] * n  # 仅以Y中顶点为中间节点时，从v0-vi的当前最短路径的长度

print(dijkstra(n, W, F))
