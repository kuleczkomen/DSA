def merge(left, right):
    res = [0 for _ in range ((len(left) + len(right)))]
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            res[i+j] = left[i]
            i += 1
        else:
            res[i+j] = right[j]
            j += 1
    #end

    while i < len(left):
        res[i+j] = left[i]
        i += 1
    while j < len(right):
        res[i+j] = right[j]
        j += 1

    return res
#end

def MergeSort(T):
    N = len(T)
    if N <= 1:
        return T
    
    mid = N//2
    left = T[mid:]
    right = T[:mid]

    left = MergeSort(left); right = MergeSort(right);

    return merge(left, right)
#end

T = [4,25,1,6,6,6,2,5,7]
print(MergeSort(T))