import itertools


def primes():
    """Yields the sequence of prime numbers via the Sieve of Eratosthenes."""
    D = {}
    yield 2
    # start counting at 3 and increment by 2
    for q in itertools.count(3, 2):
        p = D.pop(q, None)
        if p is None:
            # q not a key in D, so q is prime, therefore, yield it
            yield q
            # mark q squared as not-prime (with q as first-found prime factor)
            D[q * q] = q
        else:
            # let x <- smallest (N*p)+q which wasn't yet known to be composite
            # we just learned x is composite, with p first-found prime factor,
            # since p is the first-found prime factor of q -- find and mark it
            x = p + q
            while x in D or x % 2 == 0:
                x += p
            D[x] = p


def prime(n):
    if n < 1:
        raise ValueError("n must be >= 1 for nth_prime")
    for i, p in enumerate(primes(), 1):
        if i == n:
            return p