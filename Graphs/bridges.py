INF = float('inf')

def bridges(G):
    # assume G is an undirected graph
    V = len(G)
    visited = [False] * V
    parent = [None] * V
    d = [INF] * V
    low = [INF] * V
    bridges_list = []
    time = [0]

    def DFS(u):
        visited[u] = True
        time[0] += 1
        d[u] = low[u] = time[0]

        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                DFS(v)
                low[u] = min(low[u], low[v])

                if low[v] > d[u]:
                    bridges_list.append((u,v))
            
            elif v != parent[u]:
                low[u] = min(low[u], d[v])

    
    for u in range(V):
        if not visited[u]:
            DFS(u)
    
    return bridges_list

G = [[1, 2], [0, 3], [0, 4], [1, 5, 6], [2, 7], [3, 8], [3, 8], [4, 8], [5, 6, 7, 9], [8, 10, 11], [9, 12], [9, 12], [10, 11]]
print(bridges(G))