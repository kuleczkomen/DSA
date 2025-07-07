def euler_cycle(G,s):
    # assume the graph is eulerian and directed
    V = len(G)
    path = []

    def DFS(u):
        while G[u]:
            v = G[u].pop()
            # delete the (v,u) edge too
            for i in range(len(G[v])):
                if G[v][i] == u:
                    G[v].pop(i)
                    break
            DFS(v)
        path.append(u)
    
    DFS(s)
    path.reverse()
    return path


G = [[1,2,3], [0,3,4], [0,3,4], [0,1,2,4], [1,2,3]]
s=0
print(euler_cycle(G,s))

