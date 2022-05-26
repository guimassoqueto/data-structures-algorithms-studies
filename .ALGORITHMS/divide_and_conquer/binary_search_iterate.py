from math import floor


def binary_search(array: list, low: int, high: int, key: int):
    while low < high:
        mid = floor((low + high) / 2)

        if key == array[mid]: return mid
        elif key < array[mid]: high = mid - 1
        else: low = mid + 1


arr = [175, 351, 897, 314, 97, 23, 987, 315, 1004, 897, 698]
arr.sort()

print(arr)
print(binary_search(arr, 0, len(arr) - 1, 351))