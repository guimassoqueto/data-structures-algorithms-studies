#! /usr/bin/python3
import sys

def get_optimal_value(n, capacity, weights, values) -> None:
    if (not n) or (not capacity): return 0
        
    snapsack_value = 0
    items = len(weights) - 1

    if capacity and (capacity < weights[0]):
        snapsack_value += n * (values[-1] / (weights[-1] / capacity))
        n = 0

    if n:
        for i in range(items, -1, -1):
            while (n and capacity) and capacity >= weights[i]:
                capacity -= weights[i]
                snapsack_value += values[i]
                n -= 1
    
    return snapsack_value

if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(n, capacity, weights, values)
    print("{:.10f}".format(opt_value))
