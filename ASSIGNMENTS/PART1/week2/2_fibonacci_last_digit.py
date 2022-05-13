# Uses python3

# DONE
import sys
def get_fibonacci_last_digit_naive(n):
    if n < 2: return n
    else:
        a, b = 0, 1
        for i in range(1, n):
            c = a + b
            a, b = b, c % 10
    
        return b


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
# DONE