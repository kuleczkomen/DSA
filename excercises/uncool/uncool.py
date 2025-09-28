from egz3btesty import runtests

def is_cool(a,b,x,y):
    if (b < x) or (y < a): # rozłączne
        return True
    if (a <= x and b >= y) or (x <= a and y >= b): # jeden zawarty w drugim
        return True
    return False

def uncool(P):
    n = len(P)

    for i in range(n):
        a1,b1 = P[i]
        for j in range(i+1, n):
            a2,b2 = P[j]
            if not is_cool(a1,b1,a2,b2):
                return((i,j))
    

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( uncool, all_tests = True )