# Uses python3

# DONE
def calc_fib(n):
    if n == 0: return 0
    if n == 1 or n == 2: return 1

    fib_list = [0, 1, 1]
    count = 2

    while count < n:
        fib_list += [fib_list[-1] + fib_list[-2]]
        fib_list = fib_list[-2:]
        count += 1

    return fib_list[-1]

n = int(input())
print(calc_fib(n))
# DONE