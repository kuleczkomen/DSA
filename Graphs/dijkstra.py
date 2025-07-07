from queue import PriorityQueue
INF = float('inf')

def dijkstra(G,s):
    V = len(G)
    d = [INF] * V
    d[s] = 0

    q = PriorityQueue()
    q.put((0,s))

    while not q.empty():
        t,u = q.get()

        if t > d[u]:
            continue

        for v,w in G[u]:
            if d[u] + w < d[v]:
                d[v] = d[u] + w
                q.put((d[v], v))
    
    return d