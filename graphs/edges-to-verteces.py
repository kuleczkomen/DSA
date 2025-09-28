def get_list(L):
    N = max(max(u,v) for u,v in L) + 1
    G = [[] for _ in range(N)]

    for u,v in L:
        G[u].append(v)
    return G

G_edges = [(0,1), (0,2), (1,3), (2,3), (2,5), (3,4), (3,5), (4,6), (5,6)]
print(get_list(G_edges))