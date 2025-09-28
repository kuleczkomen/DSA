def countingSort(A, exp1):
    n = len(A)
    res = [0] * n
    cnt = [0] * 10

    for i in range(0, n):
        index = A[i] // exp1
        cnt[index % 10] += 1
    
    for i in range(1, 10):
        cnt[i] += cnt[i-1]
    
    for i in range(n-1, -1, -1):
        index = A[i] // exp1
        res[cnt[index % 10] -1] = A[i]
        cnt[index % 10] -= 1
    
    return res
#end

def radixSort(A):
    maks = max(A)

    exp = 1
    while (maks / exp) >=1:
        A = countingSort(A, exp)
        exp *= 10
    
    return A
#end

arr = [170, 45, 75, 90, 802, 24, 2, 66]

# Function Call
arr = radixSort(arr)
print(arr)