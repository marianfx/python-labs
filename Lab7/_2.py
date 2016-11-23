
import time

def executetimed(func):
    starttime = time.time()
    func()
    seconds = time.time() - starttime
    print("Time passed: %.10f" % seconds)

def isprime_eratosteene(n):
    """Returns True if n is prime.

    It uses the fact that a prime (except 2 and 3) is of form 6k - 1 or 6k + 1.
    Function looks only at divisors of this form (after checking 2 & 3).
    """
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True


def is_prime_basic(n):
    if n == 1 or n == 2 or n == 3 or n == 5:
        return True
    i = 6
    while i * i < n:
        if n % i == 0:
            return True
        i += 1
    return False





if __name__ == "__main__":
    eratostene = lambda: isprime_eratosteene(13669917)
    basic = lambda: is_prime_basic(13669917)
    executetimed(eratostene)
    executetimed(basic)
