from queue import deque
INF = float('inf')

def BFS_throttling(G,s):
    V = len(G)
    d = [INF] * V
    d[s] = 0
    q = deque([(0,0,s)]) # time, delay, vetex

    while q:
        t, delay, u = q.popleft()
        if t > d[u]:
            continue

        if delay == 0:
            for v,w in G[u]:
                if t < d[v]:
                    d[v] = t
                    q.append((t,w,v))
        
        else:
            q.append((t + 1, delay - 1, u))
    
    return d

        
