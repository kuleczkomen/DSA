from egz1Atesty import runtests
from queue import PriorityQueue
INF = float('inf')

def dijkstra(G,s,r,chased):
    d = [INF] * len(G)
    d[s] = 0
    q = PriorityQueue()
    q.put((0,s))

    while not q.empty():
        t,u = q.get()
        if t > d[u]:
           continue

        for v,w in G[u]:
            if chased: cost = 2*w + r
            else: cost = w
            
            if d[u] + cost < d[v]:
                d[v] = d[u] + cost
                q.put((d[v], v))
    return d


def gold(G,V,s,t,r):
    d1 = dijkstra(G,s,r,False)
    d2 = dijkstra(G,t,r,True)
    best = d1[t] # jeżeli nie kradnie

    for u in range(len(G)):
        curr = d1[u] + d2[u] - V[u]
        best = min(best, curr)
    
    return best



# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( gold, all_tests = True )