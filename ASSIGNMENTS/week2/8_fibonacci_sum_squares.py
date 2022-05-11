# Uses python3
from sys import stdin

# DONE
def fibonacci_sum_squares_naive(n):
    if n == 0: return 0
    if n == 1: return 1
    if n == 2: return 2

    fib_list = [0, 1, 1]
    count = 3
    total = 2
    while count <= n:
        fib_list += [fib_list[-1] + fib_list[-2]]
        total += fib_list[-1] ** 2
        fib_list = fib_list[-2:]
        count += 1

    return total % 10


if __name__ == '__main__':
    n = int(stdin.read())
    print(fibonacci_sum_squares_naive(n))
