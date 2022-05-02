def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product


def max_pairwise_product_2(numbers):
    numbers.sort()
    return numbers[-1] * numbers[-2]


##### TESTS CASES
# from random import randint
# while True:
#     array_length = randint(2, 10)
#     numbers = [randint(1, 1000) for n in range(array_length)]

#     n1 = max_pairwise_product(numbers)
#     n2 = max_pairwise_product_2(numbers)

#     if n1 != n2:
#         print(numbers)
#         print(f"max_pairwise_product: {n1}")
#         print(f"max_pairwise_product_2: {n2}\n\n")
#         break

#     print(n1, n2, "OK")


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_2(input_numbers))
