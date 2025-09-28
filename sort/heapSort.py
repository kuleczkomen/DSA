def left(i): return 2*i +1
def right(i): return 2*i +2
def parent(i): return (i-1) // 2

def heapify(T,N,i):
    l, r, max_ind = left(i), right(i), i;

    if l<N and T[l] > T[max_ind]:
        max_ind = l
    if r<N and T[r] > T[max_ind]:
        max_ind = r
    
    if max_ind != i:
        T[max_ind], T[i] = T[i], T[max_ind]
        heapify(T,N,max_ind)
    
    return T

def build_heap(T):
    N = len(T)

    for i in range(parent(N-1), -1, -1):
        heapify(T,N,i)
    
    return T

def heap_sort(T):
    N = len(T)
    build_heap(T)

    for i in range(N-1, 0, -1):
        T[i], T[0] = T[0], T[i]
        heapify(T,i,0)
    
    return T
#end


T = [8,4,3,10,2.23,2,3.01,5,1,5,-1]
print(heap_sort(T))