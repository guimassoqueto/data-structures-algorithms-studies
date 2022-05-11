# Uses python3
import sys

# DONE
def gcd_naive(a, b):
    # if a is equal b, return one of them
    if a == b: return a

    # if b is less than, b turns into a, and vice versa.
    if a < b: a, b = b, a

    # while a % b is more than 0, returns true, and the loop keeps running
    while a % b:
        # a turns into b, and b turns into a % b
        a, b = b, a % b

    return b

if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))


    

# if __name__ == "__main__":
#     input = sys.stdin.read()
#     a, b = map(int, input.split())
#     print(gcd_naive(a, b))
# DONE