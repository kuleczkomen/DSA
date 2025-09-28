def articulation(G):
    n = len(G)
    d = [None] * n
    low = [None] * n
    visited = [False] * n
    parent = [None] * n
    res = []
    time = [0]

    def DFS(u):
        visited[u] = True
        d[u] = low[u] = time[0]
        time[0] += 1
        children = 0

        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                DFS(v)        
                low[u] = min(low[u], low[v])
                children += 1

                if parent[u] != None and low[v] >= d[u]:
                    res.append(u)
            
            elif v != parent[u]:
                low[u] = min(low[u], d[v])
        
        if parent[u] is None and children > 1:
            res.append(u)
    
    DFS(0)
    return res
    
        