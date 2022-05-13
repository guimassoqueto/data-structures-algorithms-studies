def fib(n: int): 
    if n < 2: return n

    a, b = 0, 1
    arr = [0, 1]
    arr2 = [0, 1]
    for _ in range(1, n):
        a, b = b, a + b
        arr.append(b)
        arr2.append(b % 5)

    return arr, arr2
arr, arr2 = fib(50)
for i in range(0, 20):
    print(arr2[i], arr2[i + 20])

####################################################