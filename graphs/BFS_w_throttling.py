from collections import deque

def bfs_weighed(G, s):
    n = len(G)
    Q = deque()
    d = [float('inf')] * n
    
    Q.append((s, 0))  # (vertex, delay)
    d[s] = 0
    
    while Q:
        v, delay = Q.popleft()
        
        if delay > 0: # wait
            Q.append((v, delay - 1))
            continue
        
        # if delay == 0
        for u, w in G[v]:
            if d[v] + w < d[u]:
                d[u] = d[v] + w
                Q.append((u, w - 1))  # add delay (w-1)
    
    return d