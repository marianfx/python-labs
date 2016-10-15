
def isprime(n):
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


def biggestprime(text):
    """Scrieti o functie care sa returneze cel mai mare numar prim dintr-un string.

     Returneaza -1 daca sirul de caractere nu contine nici un numar prim.
     Ex:
     input: 'ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd97sidsda';
     output: 271
    """
    result = -1
    temp = ""
    for c in text:
        if c.isdigit():
            temp += str(c)
            nr = int(temp)
            if nr > result and isprime(nr):
                result = nr
        else:
            temp = ""

    return result

if __name__ == "__main__":
    print (biggestprime("ahsfaisd35biaishai23isisvdshcbsi271cidsbfsd972sidsa"))
