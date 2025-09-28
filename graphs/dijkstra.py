from queue import PriorityQueue

def get_list(L):
    N = max(max(u,v) for u,v,t in L) +1
    G = [[] for _ in range(N)]

    for u,v,t in L:
        G[u].append((v,t))
        G[v].append((u,t))
    return G

def dijkstra(L,s,f):
    G = get_list(L)
    N = len(G)

    time = [float('inf')] * N
    time[s] = 0

    q = PriorityQueue()
    q.put((0,s))

    while not q.empty():
        t,u = q.get()

        if t > time[u]:
            continue

        for v,add_time in G[u]:
            if time[u] + add_time < time[v]:
                time[v] = time[u] + add_time
                q.put((time[v], v))
    return time[f]
        


