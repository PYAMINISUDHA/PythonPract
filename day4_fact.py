def factorial(n):
    if n == 0 or n == 1:       
        return 1
    return n * factorial(n - 1)


print(factorial(5))


def sum_numbers(n):
    if n == 0:                
        return 0
    return n + sum_numbers(n - 1)


print(sum_numbers(5))
