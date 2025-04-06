from collections import deque

def BFS(G,s): #Brute Force Search
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
#end

G = [[1,3], [2], [], [4], []]
print(BFS(G,0))
