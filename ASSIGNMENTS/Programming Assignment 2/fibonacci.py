# Uses python3
def calc_fib(n):
    if n < 0: raise ValueError("Invalid input");

    fib_list = [0, 1]

    if n == 0: return fib_list[0]
    if n == 1: return fib_list

    while len(fib_list) <= n:
        fib_list.append(fib_list[-1] + fib_list[-2])
    
    return fib_list[-1]