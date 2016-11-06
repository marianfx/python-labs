
def sumacifre(n):
    if n // 10 == 0:
        return n
    return n % 10 + sumacifre(n // 10)


def tuple_suma_cifre(a, b):
    return [(x, sumacifre(x)) for x in range(a, b)]


def aparitii_cifre(a, b):
    return {x: sum([1 for nr in range(a, b) if str(x) in str(nr)]) for x in range(0, 10)}


def construieste_string(dictionar):
    lng = len([y for x in dictionar.values() for y in x])
    strng = " " * lng
    for key in dictionar.keys():
        for index in dictionar[key]:
            strng = strng[:index] + key + strng[index + 1:]
    return strng

d = {
    'A': {0},
    'n': {1},
    'a': {2, 4},
    'r': {5, 10},
    'e': {6, 9, 11},
    'm': {8},
    ' ': {3, 7},
    '.': {12}
}

if __name__ == "__main__":
    # print(tuple_suma_cifre(105, 110))
    # print(aparitii_cifre(2, 3))
    print(construieste_string(d))
