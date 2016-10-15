
def cmmdc(x, y):
    """Computes CMMDC for two numbers."""
    if y == 0:
        return x
    return cmmdc(y, x % y)


def multiplecmmdc(*list):
    """Cel mai mare divizor comun a mai multor numere

    (o functie cu nr. variabil de parametri care sa rezolve acest lucru).
    """
    if len(list) == 0:
        return -1
    if len(list) == 1:
        return list[0]
    c = list[0]
    for number in list:
        c = cmmdc(c, number)
    return c

if __name__ == "__main__":
    print (multiplecmmdc(2, 18))
