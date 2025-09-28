def kruskal(edges, n):
    parent = list(range(n))
    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u
    def union(u,v):
        pu, pv = find(u), find(v)
        if pu != pv:
            parent[pu] = pv
            return True
        return False

    mst = []
    edges.sort(key=lambda x: x[2])  # sort by weight

    for u, v, w in edges:
        if union(u, v):
            mst.append((u, v, w))

    return mst
