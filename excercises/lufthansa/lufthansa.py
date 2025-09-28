from egzP3btesty import runtests 
from queue import PriorityQueue


def lufthansa ( G ):
   n = len(G)
   weightsCnt = {}

   for u in range(n):
      for _, w in G[u]:
         weightsCnt[w] = 0

   prev = 0
   for u in range(n):
      for v,w in G[u]:
         if u > v:
            prev += w
            weightsCnt[w] += 1

   visited = [False] * n
   mst = [] # maximal spanning tree
   pq = PriorityQueue()
   pq.put((0,0,-1)) # weight, vertex, parent
   curr = 0

   while not pq.empty():
      w, u, p = pq.get()
      w *= -1

      if visited[u]:
         continue
      visited[u] = True

      if p != -1:
         mst.append((p, u, w))
         curr += w
         weightsCnt[w] -= 1
         if weightsCnt[w] == 0:
            del weightsCnt[w]
      
      for v, w in G[u]:
         if not visited[v]:
            pq.put((-w, v, u))
            
   biggestUnused = max(k for k in weightsCnt.keys())
   return prev - curr - biggestUnused  

runtests ( lufthansa, all_tests=True )