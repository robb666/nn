
def relax(u, v, c):
    if dist[u] + c < dist[v]:
        dist[v] = dist[u] + c


def map(vertex, edges):
    for _ in range(len(vertex) - 1):
        for u, v, c in edges:
            relax(u, v, c)
            
    return dist


vertex = [1, 2, 3, 4, 5, 6, 7]
edges = [(0, 1, 6),
         (0, 2, 5),
         (0, 3, 5),
         (1, 4, -1),
         (2, 1, -2),
         (2, 4, 1),
         (3, 2, -2),
         (3, 5, -1),
         (4, 6, 3),
         (5, 6, 3)]


dist = [0, float('inf'), float('inf'), float('inf'), float('inf'), float('inf'), float('inf')]

print(map(vertex, edges))

