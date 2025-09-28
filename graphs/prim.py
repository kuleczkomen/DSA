from queue import PriorityQueue

def prim_adj_list(G):
    n = len(G)
    visited = [False] * n
    mst = []
    pq = PriorityQueue()
    pq.put((0,0,-1)) # (weight, vertex, parent)

    while not pq.empty():
        w, u, p = pq.get()
        if visited[u]:
            continue
        visited[u] = True
        if p != -1:
            mst.append((p, u, w))
        for v, weight in G[u]:
            if not visited[v]:
                pq.put((weight, v, u))

    return mst
