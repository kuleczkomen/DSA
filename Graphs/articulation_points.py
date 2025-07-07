INF = float('inf')

def articulation_points(G):
    V = len(G)
    visited = [False] * V
    d = [INF] * V
    low = [INF] * V
    points = []
    time = [0]

    def DFS(u, parent):
        visited[u] = True
        time[0] += 1
        d[u] = low[u] = time[0]
        children = 0

        for v in G[u]:
            if not visited[v]:
                DFS(v, u)
                low[u] = min(low[u], low[v])

                if low[v] >= d[u] and parent != None:
                    points.append(u)
                children += 1
            
            else:
                low[u] = min(low[u], d[v])
            
        if parent is None and children >= 2 and u not in points:
                points.append(u)

    
    for u in range(V):
        if not visited[u]:
            DFS(u, None)
    
    return points


G = [[1,2], [0,2], [0,1,3,4], [2,4], [2,3]]
print(articulation_points(G))