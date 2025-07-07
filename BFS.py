from queue import deque

def BFS(G,s):
    V = len(G)
    d = [-1] * V
    d[s] = 0
    q = deque()
    q.append(s)
    
    while q:
        u = q.popleft()
        for v in G[u]:
            if d[v] == -1:
                d[v] = d[u] + 1
                q.append(v)
    
    return d


G = [[1,2,3], [], [], [4], []]
print(BFS(G,3))