
"""
Contrived example using yield.
"""


def is_multiple(n):
    return n % 3 == 0 or n % 5 == 0


def get_multiples(n, limit):
    while n < limit:
        if is_multiple(n):
            yield n
        n += 1


def sum_multiples():
    return sum(get_multiples(1, 1000))


print sum_multiples()


"""
One liner.
"""
print sum(i for i in xrange(1, 1000) if i % 3 == 0 or i % 5 == 0)
