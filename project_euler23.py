from math import floor, sqrt


def is_abundant(n):
    summation = 1
    for i in xrange(2, int(floor(sqrt(n))) + 1):
        if n % i == 0:
            summation += i
            if n / i != i:
                summation += n / i

    return n < summation


def is_abundant_sum(n, abundants):
    for abundant in abundants:
        if n - abundant in abundants:
            return True

    return False


def non_abundant_sums():
    abundants = set()
    total = 0
    for i in xrange(1, 28124):
        if not is_abundant_sum(i, abundants):
            total += i

        if is_abundant(i):
            abundants.add(i)

    return total


print non_abundant_sums()
