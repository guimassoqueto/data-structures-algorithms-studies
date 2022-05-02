def fibo(n: int) -> int:
    fibo_elements = [0, 1]

    if n == 1: return [0]
    if n == 2: return fibo_elements

    while len(fibo_elements) < n:
        fibo_elements.append(fibo_elements[-1] + fibo_elements[-2])
    
    return fibo_elements


print(fibo(100))