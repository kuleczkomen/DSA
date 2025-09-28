def stronglyConnectedComponents(G):
    n = len(G)
    visited = [False] * n
    order = []

    def dfs1(u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                dfs1(v)
        order.append(u)

    for i in range(n):
        if not visited[i]:
            dfs1(i)

    # Reverse graph
    GR = [[] for _ in range(n)]
    for u in range(n):
        for v in G[u]:
            GR[v].append(u)

    visited = [False] * n
    sccs = []

    def dfs2(u, comp):
        visited[u] = True
        comp.append(u)
        for v in GR[u]:
            if not visited[v]:
                dfs2(v, comp)

    for u in reversed(order):
        if not visited[u]:
            comp = []
            dfs2(u, comp)
            sccs.append(comp)

    return sccs
