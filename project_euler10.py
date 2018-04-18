from math import floor, sqrt


def is_prime(n):
    if n == 2:
        return True

    for i in xrange(2, int(floor(sqrt(n))) + 1):
        if n % i == 0:
            return False

    return True


def get_primes(number, limit):
    while number < limit:
        if is_prime(number):
            yield number
        number += 1


def sum_primes():
    return sum(get_primes(2, 2000000))


print sum_primes()
