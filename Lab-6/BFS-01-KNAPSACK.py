import heapq

# item information
weight = [2, 5, 10, 5]
value = [40, 30, 50, 10]

# max weight
W = 16

n = len(weight)
# current weight and value
cweight = 0
cvalue = 0

# optimal value
bestv = 0
bests = []
num = 0
heap = []
heapq.heapify


# upperbound：compute the upperbound of current node
def upperbound(i):
    global cweight
    global cvalue
    global n
    global weight
    global value
    global W
    left = W - cweight
    b = cvalue
    while i < n and weight[i] <= left:
        left -= weight[i]
        b += value[i]
        i += 1
    if i < n:
        b += (value[i] / weight[i]) * left
    return b


i = 0
upper = upperbound(i)
str = ''

while (1):
    wt = cweight + weight[i]

    if wt <= W:
        if cvalue + value[i] > bestv:
            bestv = cvalue + value[i]
            bests = str + '1'
            bests = bests + '0' * (n - len(bests))

        if i + 1 < n:
            heapq.heappush(heap, [1 / upper, cweight + weight[i], cvalue + value[i], i + 1, str + '1'])

    upper = upperbound(i + 1)
    if upper >= bestv:
        if i + 1 < n:
            heapq.heappush(heap, [1 / upper, cweight, cvalue, i + 1, str + '0'])

    if len(heap) == 0:
        print("The optimal value is: %d" % bestv)
        break

    node = heapq.heappop(heap)
    upper = 1 / node[0]
    cweight = node[1]
    cvalue = node[2]
    i = node[3]
    str = node[4]
