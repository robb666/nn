

def relax(u, v, c):
    # print(dist[u])
    if dist[u] + c < dist[v]:
        dist[v] = dist[u] + c
        # parent[v] = u


def map(vertex, edges):
    for _ in range(len(vertex) - 1):
        for u, v, c in edges:
            relax(u, v, c)
            
    return dist


vertex = [1, 2, 3, 4, 5, 6]
edges = [(1, 2, 6),
         (1, 3, 5),
         (1, 4, 5),
         (2, 5, -1),
         (3, 2, -2),
         (3, 5, 1),
         (4, 3, -2),
         (4, 6, -1),
         (5, 7, 3),
         (6, 7, 3)]


dist = [0, 1, 2, 3, 4, 5, 6, 7, 8]
# dist[0] = 0
dist[1] = 0
dist[2] = float('inf')
dist[3] = float('inf')
dist[4] = float('inf')
dist[5] = float('inf')
dist[6] = float('inf')
dist[7] = float('inf')


print(dist)

print(map(vertex, edges))




# edges = [(0, 1, 4),
#          (0, 2, 5),
#          (0, 3, 8),
#          (1, 2, -3),
#          (2, 4, 4),
#          (3, 4, 2),
#          (4, 3, 1)]