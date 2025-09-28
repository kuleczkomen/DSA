def dijkstraMatrix(G, start): 
    n = len(G)
    d = [float('inf')] * n 
    d[start] = 0; visited = [False] * n 

    for _ in range(n): 
        u = -1; min_d = float('inf') 

        for i in range(n): 
            if not visited[i] and d[i] < min_d: 
                min_d = d[i]; u = i 

        if u == -1: break 

        visited[u] = True 
        for v in range(n): 
            if G[u][v] != 0 and not visited[v]: 
                new_d = d[u] + G[u][v] 
                if new_d < d[v]: d[v] = new_d 
    return d 