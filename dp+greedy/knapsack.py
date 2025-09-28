# F[i][b] = max suma cen przedmiotów ze zbioru {0...i}
# których łączna cena nie przekracza b

def knapsack(W,P,B):
    n = len(W)
    F = [[0]*(B+1) for _ in range(n)]

    for b in range(W[0], B+1):
        F[0][b] = P[0]
    
    for b in range(B+1):
        for i in range(1,n):
            F[i][b] = F[i-1][b]
            if b >= W[i]:
                F[i][b] = max(F[i][b], F[i-1][b-W[i]] + P[i])
    
    return F[n-1][B]

W = [2, 3, 4, 5]      # weights
P = [3, 4, 6, 6]      # values (profits)
B = 5                # capacity

print(knapsack(W,P,B))