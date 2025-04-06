# BFS + zapisz, z którego wierzchołka przeszłeś (będzie odwrócona kolejność)

from collections import deque

def find_path(G,s,f): # s-start, f-finish
    if s==f:
        return "same vertex"
    
    visited = [False] * len(G)
    visited[s] = True
    parent = [None] * len(G)
    path = []

    q = deque([s])

    while q:
        u = q.popleft()

        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                q.append(v)

                if v == f:
                    path = [v]
                    while v != s:
                        path.append(parent[v])
                        v = parent[v]
                    return path[::-1]
    return "no path"
#end

start = 0
finish = 3

G = [[1,5], [2], [3], [4], [], [4]]
print(find_path(G,start,finish))
                
                
    




