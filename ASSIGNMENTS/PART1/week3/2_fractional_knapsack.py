#! /bin/python3

import sys
# The first line of the input contains the number 𝑛 of items and the capacity 𝑊 of a knapsack.
# The next 𝑛 lines define the values and weights of the items. The 𝑖-th line contains integers 𝑣 𝑖 and 𝑤 𝑖 —the
# value and the weight of 𝑖-th item, respectively.

# n = number of items of the knapsack
# capacity = capacity of the bag

# values = value of the items
# weights = weight of the items


def get_optimal_value(capacity, weights, values):
    zipped = list(zip(values, weights))

    # sort list based on the first element of the tuple, in this case, item's value
    zipped.sort(key = lambda item: item[0], reverse=True)
    
    snapsack_value = 0
    for item_value, item_weight in zipped:
        while(capacity >= item_weight):
            capacity -= item_weight
            snapsack_value += item_value
    
    if capacity > 0:
        # most valuable item is the first, since the list is sorted based on values
        item_value, item_weight = zipped[0]
        snapsack_value += (capacity / item_weight) * item_value

    print(capacity, snapsack_value)


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    #print("{:.10f}".format(opt_value))
