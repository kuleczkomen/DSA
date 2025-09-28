# F[i][j] = min koszt, za jaki można się dostać do i-tej planety,
# mając w baku j ton paliwa

# F[i][j] = min(F[i][j-1] + C[i], F[i-1][j+d])

def planets(D,C,T,E):
    n = len(D)
    INF = float('inf')
    F = [[INF]*(E+1) for _ in range(n)]

    for i in range(E+1):
        F[0][i] = i * C[i]

    for i in range(1,n):
        d = D[i] - D[i-1]
        F[i][0] = min(F[i][0], F[i-1][d])

        for j in range(1,E+1):
            if j+d <= E: #   bez zmian,   tankowanie,    przylot z paliwem  
                F[i][j] = min(F[i][j], F[i][j-1] + C[i], F[i-1][j+d])
            else:
                F[i][j] = min(F[i][j],F[i][j-1] + C[i])
        
        tele_planet, tele_cost = T[i]

        if tele_planet >= i:
            F[tele_planet][0] = min(F[tele_planet][0], F[i][0] + tele_cost)


# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( planets, all_tests = True )