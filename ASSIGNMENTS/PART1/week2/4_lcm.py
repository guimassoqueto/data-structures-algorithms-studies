# Uses python3
import sys

#DONE
def lcm_naive(a, b):
    if a == b: return a
    if a < b: a, b = b, a

    # a * b if for sure a multiple of a and b
    c = a * b 

    # now you turn b into the maximum divisor between a and b
    while a % b:
        a, b = b, a % b
    
    return int(c / b)

if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))
# done