import random

def quicksort(T, low=0, high=None):
    if high is None:
        high = len(T) - 1
    
    if low < high:
        p = random_partition(T, low, high)
        quicksort(T, low, p - 1)
        quicksort(T, p + 1, high)

def random_partition(T, low, high):
    pivot_index = random.randint(low, high)
    T[pivot_index], T[high] = T[high], T[pivot_index]
    return partition(T, low, high)

def partition(T, low, high):
    pivot = T[high]
    i = low - 1
    for j in range(low, high):
        if T[j] <= pivot:
            i += 1
            T[i], T[j] = T[j], T[i]
    T[i+1], T[high] = T[high], T[i+1]
    return i + 1


T = [7,5,1,8,9,2,11,6]
quicksort(T)
print(T)
