#! /usr/bin/python3
import sys

def get_optimal_value(n, capacity, weights, values) -> None:
    if (n <= 0) or (capacity <= 0): return 0

    ratio_vw = [(weights[i], values[i], values[i] / weights[i]) for i in range(len(weights))]
    ratio_vw.sort(key = lambda tup: tup[2], reverse=True)

    snappack_value = 0
    remaining_items = []
    for i in range(len(ratio_vw)):
        w, v, r = ratio_vw[i]
        if capacity >= w:
            capacity -= w
            snappack_value += v
        else: remaining_items.append((w, v, r))
        
    del ratio_vw

    if capacity and len(remaining_items):
        snappack_value += capacity / remaining_items[0][0] * remaining_items[0][1]

    return snappack_value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(n, capacity, weights, values)
    print("{:.10f}".format(opt_value))
