from queue import PriorityQueue
INF = float('inf')
I = 0
P = 1

def graph(E):
    V = max(max(u,v) for u,v,w,type in E) + 1
    G = [[] for _ in range(V)]

    for u,v,w,type in E:
        if type == 'P': 
            G[u].append((v,w,P))
            G[v].append((u,w,P))
        else:
           G[u].append((v,w,I))
           G[v].append((u,w,I))
    return G

def dijkstra(G,A):
    d = [ [INF]*2 for _ in range(len(G)) ]
    d[A][0] = d[A][1] = 0
    q = PriorityQueue()
    
    for v,w,type in G[A]:
       q.put((w,v,type))
       d[v][type] = w
    
    while not q.empty():
        t,u,old_type = q.get()
        if t > d[u][old_type]:
            continue

        for v,w,new_type in G[u]:
            if old_type == new_type == I: add = 5
            elif old_type == new_type == P: add = 10
            else: add = 20

            if d[u][old_type] + w + add < d[v][new_type]:
                d[v][new_type] = d[u][old_type] + w + add
                q.put((d[v][new_type], v, new_type))
    
    return d


def tory_amos( E, A, B ):
    G = graph(E)
    d = dijkstra(G,A)
    return min(d[B])


from egz2btesty import runtests
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( tory_amos, all_tests = True )
