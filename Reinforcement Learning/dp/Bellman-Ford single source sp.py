

def relax(dist, u, v, c):
    if dist[u] + c < dist[v]:
        dist[v] = dist[u] + c
        # parent[v] = u


def map(dist, vertex, edges):
    for _ in range(len(vertex) - 1):
        for u, v, c in edges:
            relax(dist, u, v, c)
            
    return dist


vertex = [0, 1, 2, 3, 4, 5]
edges = [(0, 1, 4), (0, 2, 5), (0, 3, 6), (1, 2, -3),
         (2, 5, 4), (3, 4, 2), (4, 5, 2), (5, 4, 1)]

dist = [0, 1, 2, 3, 4, 5]
dist[0] = 0
dist[1] = float('inf')
dist[2] = float('inf')
dist[3] = float('inf')
dist[4] = float('inf')
dist[5] = float('inf')


print(dist)

print(map(dist, vertex, edges))

