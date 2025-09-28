# F[i][k] = maks wartość ciągu od i do j, jeżeli usuniemy max k elementów

# F[i][k] = max(F[i-1][k] + T[i], T[i], F[i-1][k-1])
#                kontynuuj,  nowy,  pomiń

def kstrong(T,k):
    n = len(T)
    INF = float('inf')
    F = [[-INF]*(k+1) for _ in range(n)]
    F[0][0] = T[0]

    for j in range(1,k+1):
        F[0][j] = max(0, F[0][j-1])

    for i in range(1,n):
        F[i][0] = T[i] + max(F[i-1][0], 0)
        for j in range(1,k+1):
            F[i][j] = max(F[i-1][j] + T[i], T[i], F[i-1][j-1])
        
    return max(max(F[i]) for i in range(n))

from egz1btesty import runtests
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( kstrong, all_tests = True )