function binary_search<T>(arr: Array<T>, low: number, high: number, key: T) {
    if (high < low) return -1

    const mid = Math.floor((low + high) / 2)

    if (arr[mid] == key) return mid
    if (arr[mid] < key) return binary_search(arr, 0, mid - 1, key)
    if (arr[mid] > key) return binary_search(arr, mid + 1, high, key)
    return - 1
}

const array: number[] = [175, 351, 897, 314, 97, 23, 987, 315, 1004, 897, 698]
array.sort((a, b) => a - b)

console.log(array)
console.log(binary_search<number>(array, 0, array.length, 315))