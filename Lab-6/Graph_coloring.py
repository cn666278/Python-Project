# m_coloring problem

def m_coloring(i):

    if promising(i):
        if i == n:  # last node
            # print(vcolor)
            for i in range(1, n+1):
                print(vcolor[i], end=",")
            print("\n")
        else:
            for color in range(1, m+1):   # try every color for next node
                vcolor[i + 1] = color
                m_coloring(i + 1)

def promising(i):
    j = 1
    flag = True

    while j < i and flag:  # i:current node;  j:previous node
        if W[i][j] and vcolor[i] == vcolor[j]:  # connected and same color
            flag = False  # dead end
        j += 1

    return flag


m = 3   # number of colors
n = 4   # number of nodes

# W is the adjacent matrix that index from 1 to n
W = [                   # j start from 1
    [0, 0, 0, 0, 0],
    [0, 0, 1, 1, 1],
    [0, 1, 0, 1, 0],
    [0, 1, 1, 0, 1],
    [0, 1, 0, 1, 0],
]

vcolor = [0] * (n + 1)  # vector[i] is the color assign to node i
m_coloring(0)  # top level call
