from egzP5atesty import runtests 

def inwestor ( T ):
   best = 0
   stack = [(0, T[0])] # (start, height)

   for i in range(1, len(T)):
      if stack:
         start = i
         while stack and T[i] < stack[-1][1]:
            start = stack[-1][0]
            best = max(best, stack[-1][1] * (i - stack[-1][0]))
            stack.pop()
         stack.append((start, T[i]))
   
   while stack:
      best = max(best, stack[-1][1] * (len(T) - stack[-1][0]))
      stack.pop()
   
   return best

runtests ( inwestor, all_tests=True )