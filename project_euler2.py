

def even_fibonaccis(a, b):
    while b < 4000000:
        a, b = b, a + b
        if not b % 2:
            yield b


def even_fibonacci_sum():
    return sum(even_fibonaccis(0, 1))


print even_fibonacci_sum()
