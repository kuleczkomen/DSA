def dfs(G,s):
    n = len(G)
    d = [None] * n
    visited = [False] * n
    parent = [None] * n
    time = [0]

    def dfsVisit(u):
        visited[u] = True
        d[u] = time[0]
        time[0] += 1

        for v in G[u]:
            if not visited[v]:
                parent[v] = u
                dfsVisit(v)
    dfsVisit(s)
    return d, parent, visited

G = [[1,3], [2], [], [4], []]
print(dfs(G,0)) 