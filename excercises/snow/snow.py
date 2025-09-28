from egz1atesty import runtests

def snow( S ):
    n = len(S)
    best_snow = 0
    d = 0
    S = sorted(S, key=lambda x: -x)
    for i in range(n):
        if S[i] - d > 0:
            best_snow += S[i] - d
            d += 1
            S[i] = 0
    return best_snow

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( snow, all_tests = False )
