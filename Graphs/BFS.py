from collections import deque

def BFS(G,s):
    V = len(G)
    visited = [False] * V
    d = [-1] * V
    parent = [None] * V

    q = deque()
    q.append(s)
    d[s] = 0

    while q:
        u = q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                d[v] = d[u] + 1
                parent[v] = u
    
    return d, parent, visited