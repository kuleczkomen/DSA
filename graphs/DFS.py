def DFS(G,s):
    V = len(G)
    visited = [False] * V
    parent = [None] * V
    time = [-1] * V
    stack = [s]
    visited[s] = True
    time[s] = 0

    while stack:
        u = stack.pop()
        for v in reversed(G[u]):
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                time[v] = time[u] + 1
                stack.append(v)
    return visited, parent, time

G = [[1,3], [2], [], [4], []]
print(DFS(G,0))