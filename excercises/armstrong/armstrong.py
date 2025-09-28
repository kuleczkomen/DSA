from queue import PriorityQueue
INF = float('inf')

def graph(G):
    V = max(max(u,v) for u,v,w in G) + 1
    A = [[] for _ in range(V)]

    for u,v,w in G:
        A[u].append((v,w))
        A[v].append((u,w))
    
    return A

def dijkstra(G, s):
    d = [INF] * len(G)
    d[s] = 0
    q = PriorityQueue()
    q.put((0,s))

    while not q.empty():
        t,u = q.get()
        if t > d[u]: continue

        for v,w in G[u]:
            if d[u] + w < d[v]:
                d[v] = d[u] + w
                q.put((d[v], v))
    return d

def bikes(B,V):
    b = [1] * V

    for i,p,q in B:
        b[i] = min(b[i], p/q)
    return b


def armstrong(B,G,s,t):
    G = graph(G)
    V = len(G)
    B = bikes(B, V)
    d1 = dijkstra(G,s)
    d2 = dijkstra(G,t)
    d = [INF] * V

    for i in range(V):
        d[i] = d1[i] + B[i]*d2[i]
    
    return int(min(d))
        

from egz1atesty import runtests
runtests( armstrong, all_tests = True )
