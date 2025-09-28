"""
d[i][j] = min koszt dotarcia do wierzchołka i, docierając j-tym typem torów
"""
from egz2btesty import runtests
from queue import deque

P, I = 0, 1
INF = float('inf')

def graph(E):
  V = max(max(u,v) for u,v,_,_ in E) + 1
  G = [[] for _ in range(V)]

  for u,v,w,t in E:
    typ = P if t == 'P' else I
    G[u].append((v,w,typ))
    G[v].append((u,w,typ))
    
  return G


def tory_amos( E, A, B ):
  G = graph(E)
  V = len(G)

  d = [[INF] * 2 for _ in range(V)]
  d[A][0] = d[A][1] = 0

  q = deque()
  
  for v,w,typ in G[A]: 
    # wyruszamy ze stacji A w każdym możliwym kierunku
    d[v][typ] = w
    q.append((w, v, typ))

  while q:
    t, u, currType = q.popleft()

    if t > d[u][currType]:
      continue

    for v, w, newType in G[u]:
      if currType == newType == P: cost = 10
      elif currType == newType == I: cost = 5
      else: cost = 20

      currTime = d[u][currType] + w + cost
      if currTime < d[v][newType]:
        d[v][newType] = currTime
        if w + cost <= 10:  
          q.appendleft((d[v][newType], v, newType))
        else:
          q.append((d[v][newType], v, newType))

  return min(d[B])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( tory_amos, all_tests = True )
