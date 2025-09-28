def magic(C):
    n = len(C)
    F = [-1] * n
    F[0] = 0

    for i in range(n):
        if F[i] == -1:
            continue
        gold = C[i][0]

        for j in range(1, 4):  
            room = C[i][j][1]
            cost = C[i][j][0]

            if room > i and gold - cost <= 10:
                F[room] = max(F[room], F[i] + gold - cost)
    return F[n-1]


from egz2btesty import runtests
# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( magic, all_tests = True )
