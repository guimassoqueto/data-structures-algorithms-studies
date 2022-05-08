# Uses python3
import sys

def gcd(a, b):
    while b:
        a, b = b, a%b
    return a

print(gcd(0, 32))