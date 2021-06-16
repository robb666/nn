

def relax(u, v, c):
    if d[v] > d[v] + c(u, v):
        d[v] = d[v] + c(u, v)
        parent[v] = u


def map(v, edges):
    for i in range(1, len(v) - 1):
        for e in edges:
            relax(u, v, w)



v = [0, 1, 2, 3, 4]
edges = [(0, 1), (0, 2), (0, 3), (1, 2), (2, 4), (3, 4), (4, 3)]








