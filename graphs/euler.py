def Euler_cycle(G):
    n = len(G)
    
    def connected(G):
        visited = [False]*n
        def dfs(u):
            visited[u] = True
            for v in G[u]:
                if not visited[v]:
                    dfs(v)
        dfs(0)
        return all(visited)
    
    if not connected(G):
        return False
    
    for adj in G:
        if len(adj) % 2 != 0:
            return False

    # Copy adjacency list so we can modify it
    graph = [neighbors[:] for neighbors in G]

    stack = [0]
    path = []

    while stack:
        u = stack[-1]
        if graph[u]:
            v = graph[u].pop()
            # Remove edge in both directions
            graph[v].remove(u)
            stack.append(v)
        else:
            path.append(stack.pop())
    
    return path[::-1]


G = [[1,2], [0,2], [0,1,3,4], [2,4], [2,3]]
print(Euler_cycle(G))

