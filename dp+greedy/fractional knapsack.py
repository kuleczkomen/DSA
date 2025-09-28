def fractional_knapsack(values, weights, capacity):
    items = sorted(
        ((v / w, v, w) for v, w in zip(values, weights)),
        reverse=True
    )
    
    total_value = 0.0
    for ratio, value, weight in items:
        if capacity >= weight:
            total_value += value
            capacity -= weight
        else:
            total_value += ratio * capacity
            break
    return total_value

# Przykład
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

result = fractional_knapsack(values, weights, capacity)
print("Maksymalna wartość:", result)
