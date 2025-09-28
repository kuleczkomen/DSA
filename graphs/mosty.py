def bridge(G):
    n = len(G)
    d = [None] * n
    low = [None] * n
    visited = [False] * n
    parent = [None] * n
    bridges = []
    time = [0]

    def dfs(u):
        visited[u] = True
        d[u] = low[u] = time[0]
        time[0] += 1

        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                dfs(v)
                low[u] = min(low[u], low[v])

                if low[v] > d[u]:
                    bridges.append((u, v))
            elif v != parent[u]:
                low[u] = min(low[u], d[v])

    dfs(0)
    return bridges

    
        