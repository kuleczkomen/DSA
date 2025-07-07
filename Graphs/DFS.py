def DFS(G,s):
    V = len(G)
    visited = [False] * V
    parent = [None] * V
    d = [-1] * V
    
    visited[s] = True
    d[s] = 0

    stack = []
    stack.append(s)

    while stack:
        u = stack.pop()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                d[v] = d[u] + 1
                stack.append(v)
    
    return d, parent, visited