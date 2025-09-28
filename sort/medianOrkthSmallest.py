def select(arr, k):
    if len(arr) <= 5:
        return sorted(arr)[k]

    medians = [sorted(arr[i:i+5])[len(arr[i:i+5])//2] for i in range(0, len(arr), 5)]
    pivot = select(medians, len(medians)//2)

    lows = [x for x in arr if x < pivot]
    highs = [x for x in arr if x > pivot]
    pivots = [x for x in arr if x == pivot]

    if k < len(lows): return select(lows, k)
    elif k < len(lows) + len(pivots): return pivot
    else: return select(highs, k - len(lows) - len(pivots))
