# Uses python3
import sys
#done
def get_fibonacci_huge_naive(n, m):
    if n == 0: return 0
    if n == 1: return 1

    a, b = 0, 1
    for _ in range(1, n):
        a, b = b, a + b
        
    return b % m

get_fibonacci_huge_naive(9999999999999, 2)

# if __name__ == '__main__':
#     input = sys.stdin.read();
#     n, m = map(int, input.split())
#     print(get_fibonacci_huge_naive(n, m))
# done