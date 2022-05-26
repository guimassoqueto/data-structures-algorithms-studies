function binary_search_iterate<T>(arr: Array<T>, low: number, high: number, key: T) {
    while (low < high) {
        const mid = Math.floor((low + high) / 2)

        if (arr[mid] == key) return mid
        else if (arr[mid] < key) high = mid - 1
        else low = mid + 1
    }
    return -1
}

const arr: number[] = [175, 351, 897, 314, 97, 23, 987, 315, 1004, 897, 698]
arr.sort((a, b) => a - b)

console.log(arr)
console.log(binary_search_iterate<number>(arr, 0, arr.length, 315))