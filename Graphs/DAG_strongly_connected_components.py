from queue import deque
INF = float('inf')

def reverse(G):
    V = len(G)
    H = [[] for _ in range(V)]
    for u in range(V):
        for v in G[u]:
            H[v].append(u)
    return H


def SCC(G):
    # assume G is a directed graph
    V = len(G)
    visited = [False] * V
    order = []

    def DFS(u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFS(v)
        order.append(u)
    
    for u in range(V): # if the graph isn't connected
        if not visited[u]:
            DFS(u)

    G = reverse(G)

    visited = [False] * V
    components = []
    
    def DFS2(u, comp):
        visited[u] = True
        comp.append(u)
        for v in G[u]:
            if not visited[v]:
                DFS2(v, comp)
    
    for u in reversed(order):
        if not visited[u]:
            comp = []
            DFS2(u, comp)
            components.append(comp)

    return components


G = [[1], [2], [0,3], [6], [3], [4], [5]]
print(SCC(G))

    