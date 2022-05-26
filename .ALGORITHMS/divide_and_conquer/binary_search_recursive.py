from math import floor


def binary_search(array: list, low: int, high: int, key: int):
    if high < low: return -1

    mid = floor((low + high) / 2)

    if array[mid] == key: return mid
    if key < array[mid]: return binary_search(array, 0, mid - 1, key)
    if key > array[mid]: return binary_search(array, mid + 1, high, key)

    return -1


arr = [175, 351, 897, 314, 97, 23, 987, 315, 1004, 897, 698]
arr.sort()

print(arr)
print(binary_search(arr, 0, len(arr) - 1, 351))