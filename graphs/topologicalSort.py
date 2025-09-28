def topological_sort(G):
    visited = [False] * len(G)
    order = []

    def DFS_visit(u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFS_visit(v)
        order.append(u)

    for i in range(len(G)):
        if not visited[i]:
            DFS_visit(i)

    return order[::-1]  

