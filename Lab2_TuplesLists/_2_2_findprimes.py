
def isprime(n):
    """Returns True if n is prime.

    It uses the fact that a prime (except 2 and 3)
    is of form 6k - 1 or 6k + 1 and looks only at divisors of this form.
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


def filterByPrimes(list):
    """Sa se scrie o functie care primeste o lista de numere.

    Returneaza o lista cu numerele prime care se gasesc in ea.
    """
    return filter(isprime, list)

if __name__ == "__main__":
    print (filterByPrimes([1, 5, 7, 8, 9, 14, 15, 17, 91]))
