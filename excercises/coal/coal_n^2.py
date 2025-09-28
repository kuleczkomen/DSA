def coal(A,T):
    n = len(A)
    W = [0] * n

    for i in range(n):
        for j in range(n):
            if A[i] + W[j] <= T:
                W[j] += A[i]
                break  
    return j

from egz2atesty import runtests
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( coal, all_tests = True )
