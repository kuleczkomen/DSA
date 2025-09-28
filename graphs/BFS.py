from collections import deque

def BFS(G,s):
    visited = [False] * len(G)
    parent = [None] * len(G)
    time = [float('inf')] * len(G)
    q = deque([s])
    visited[s] = True; time[s] = 0

    while q:
        u = q.popleft()
        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                time[v] = time[u] +1
                q.append(v)
    return visited, parent, time
