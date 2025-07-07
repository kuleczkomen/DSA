def topological_sort(G,s):
    V = len(G)
    visited = [False] * V
    stack = [(s, False)]
    res = []

    while stack:
        u, processed = stack.pop()

        if processed:
            visited[u] = True
            res.append(u)
        
        elif not visited[u]:
            stack.append((u, True))
            for v in reversed(G[u]):
                if not visited[v]:
                    stack.append((v, False))
        
    return res[::-1]

G = [[1,2], [2,4], [], [], [3,5,6], [], []]
s = 0
print(topological_sort(G,s))