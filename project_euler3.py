from math import ceil, floor, sqrt


def is_prime(n):
    if n == 2:
        return True

    for i in xrange(2, int(floor(sqrt(n))) + 1):
        if n % i == 0:
            return False

    return True


def fermat_factorization(n):
    a = int(ceil(sqrt(n)))
    b = a * a - n
    while not sqrt(b).is_integer():
        a = a + 1
        b = a * a - n

    return int(a - sqrt(b)), int(a + sqrt(b))


def largest_prime_factorization(n):
    a, b = fermat_factorization(n)
    if a not in factors:
        if is_prime(a):
            factors.add(a)
        else:
            largest_prime_factorization(a)

    if b not in factors:
        if is_prime(b):
            factors.add(b)
        else:
            largest_prime_factorization(b)

factors = set()
largest_prime_factorization(600851475143)
print max(factors)
