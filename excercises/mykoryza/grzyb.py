from egz3atesty import runtests
from queue import deque

def mykoryza( G,T,d ):
    n = len(T)
    fungus = [0] * n
    visited = [False] * len(G)
    q = deque()

    for i in range(n):
        fungus[i] = 1
        q.append((T[i], i)) # vertex, fungus
        visited[T[i]] = True
    
    while q:
        u, g = q.popleft()

        for v in G[u]:
            if not visited[v]:
                visited[v] = True
                fungus[g] += 1
                q.append((v, g))

    return fungus[d]

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( mykoryza, all_tests = True )
