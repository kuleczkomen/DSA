def countingSort(A):
    k = max(A); n = len(A); B = [None] * n; C = [0] * (k+1)
    for i in A: C[i] += 1
    for i in range(1,k+1): C[i] += C[i-1]
    for i in range(n-1, -1, -1):
        B[C[A[i]] -1] = A[i]; C[A[i]] -= 1
    return B
#end

A = [2,1,0,9,6,1,5,12]
print(countingSort(A))