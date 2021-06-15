

def relax(u, v, c):
    if d[v] > d[v] + c(u, v):
        d[v] = d[v] + c(u, v)


def initialize(v, edges):
    for i in range(1, len(v) - 1):
        for e in edges:
            relax(u, v, w)




edges = []






