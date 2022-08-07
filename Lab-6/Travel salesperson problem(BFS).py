# 分支限界法求解旅行商问题
import math
from heapq import *


class Node:

    def __init__(self, w=math.inf, route=[], cost=0):
        self.weight = w
        self.route = route
        self.cost = cost

    def __lt__(self, other):
        return int(self.weight) < int(other.weight)

    # print
    def __str__(self):
        return "node weight is" + str(self.weight) + " path is" + str(self.route) + " cost is" + str(self.cost)


def BBTSP(graph, n, s):
    global bestcost, bestroute
    heap = []

    start = Node(route=[str(s)])
    heap.append(start)


    while heap:
        nownode = heappop(heap)
        # Generate the lower node of the number with the highest weight and add the lower node to the heap
        for e in [r for r in graph if r not in nownode.route]:
            node = Node(w=graph[nownode.route[-1]][e], route=nownode.route + [e],
                        cost=nownode.cost + graph[nownode.route[-1]][e])
            # If the current value is greater than the optimal value, prune
            if node.cost >= bestcost:
                continue
            # If you reach the last point, add the way back and calculate the minimum
            if len(node.route) == n:
                wholecost = graph[node.route[-1]][s] + node.cost
                if wholecost < bestcost:
                    bestcost = wholecost
                    bestroute = node.route
                    print("The optimal cost is:" + str(bestcost))
                    print("The best path is:" + str(bestroute))

            heap.append(node)

    return bestcost

n = 5
x = [1, 2, 3, 4, 5]

G = {
    '1': {'2': 14, '3': 4, '4': 10, '5': 20},
    '2': {'1': 14, '3': 7, '4': 8, '5': 7},
    '3': {'1': 4, '2': 5, '4': 7, '5': 16},
    '4': {'1': 11, '2': 7, '3': 9, '5': 2},
    '5': {'1': 18, '2': 7, '3': 17, '4': 4},
}

graph = [
    [0, 14, 4, 10, 20],
    [14, 0, 7, 8, 7],
    [4, 5, 0, 7, 16],
    [11, 7, 9, 0, 2],
    [18, 7, 17, 4, 0]
]

bestcost = math.inf
nowcost = 0

BBTSP(G, n, '1')
