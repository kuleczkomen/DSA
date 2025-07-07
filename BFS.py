from queue import deque
INF = float('inf')

def BFS(G,s):
    V = len(G)
    d = [INF] * V
    d[s] = 0
    q = deque()
    q.append(s)
    
    while q:
        u = q.popleft()
        for v in G[u]:
            if d[v] == INF:
                d[v] = d[u] + 1
                q.append(v)
    
    return d


G = [[1,2,3], [], [], [4], [5], []]
print(BFS(G,0))