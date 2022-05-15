#! /bin/python3

import sys
# Task. Given two sequences 𝑎 1 , 𝑎 2 , . . . , 𝑎 𝑛 (𝑎 𝑖 is the profit per click of the 𝑖-th ad) and 𝑏 1 , 𝑏 2 , . . . , 𝑏 𝑛 (𝑏 𝑖 is
# the average number of clicks per day of the 𝑖-th slot), we need to partition them into 𝑛 pairs (𝑎 𝑖 , 𝑏 𝑗 )
# such that the sum of their products is maximized.

# Input Format. The first line contains an integer 𝑛, the second one contains a sequence of integers
# 𝑎 1 , 𝑎 2 , . . . , 𝑎 𝑛 , the third one contains a sequence of integers 𝑏 1 , 𝑏 2 , . . . , 𝑏 𝑛 .

# done
def max_dot_product(a, b):
    #write your code here
    a.sort()
    b.sort()

    total = 0
    for i in range(len(a)):
        total += a[i] * b[i]

    return total

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    a = data[1:(n + 1)]
    b = data[(n + 1):]
    print(max_dot_product(a, b))
# done
