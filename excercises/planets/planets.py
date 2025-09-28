from egz1btesty import runtests

def planets( D, C, T, E ):
    n = len(T)
    INF = float('inf')
    F = [[INF]*(E+1) for _ in range(n)]
    
    for i in range(E+1):
        F[0][i] = C[0] * i
    
    tele_planet, tele_cost = T[0]
    F[tele_planet][0] = min(F[tele_planet][0], tele_cost)

    for i in range(1, n):
        d = D[i] - D[i-1]
        F[i][0] = min(F[i-1][d], F[i][0])  # dojechanie na pustym baku

        for j in range(1, E+1):
            if d+j <= E:  # bez zmian; bez tankowania; z tankowaniem
                F[i][j] = min(F[i][j], F[i-1][d+j], F[i-1][d+j-1] + C[i])
                
            F[i][j] = min(F[i][j], F[i][j-1] + C[i])  # trzeba zatankować    
        
        # teleportacja
        tele_planet, tele_cost = T[i]
        F[tele_planet][0] = min(F[tele_planet][0], F[i][0] + tele_cost)

    return min(F[n-1])

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )
