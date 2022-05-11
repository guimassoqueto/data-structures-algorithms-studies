# Uses python3
import sys

# DONE
def fibonacci_sum_naive(n):
    if n == 0: return 0
    if n == 1: return 1

    a, b = 0, 1
    c = a + b

    for _ in range(1, n):
        a, b = b, a + b
        c += b

    return c % 10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
# DONE