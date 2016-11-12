
def sort_key(string):
    """If string is valid returns string[1][2].

    We need the 3rd char of the 2nd string tuple,
    so we need length bigger than 1
    and length of the 2nd element bigger than 2.
    Return None otherwise.
    """
    if len(string) < 2:
        return None
    if len(string[1]) < 3:
        return None
    return string[1][2]


def sort_by_third(list):
    """Să se scrie o funție ce va ordona o listă de tuple de string-uri.

    Ordonarea se va face în funcție de al 3-lea caracter
    al celui de-al 2-lea element din tuplă.
    Exemplu:
    [('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]
    """
    list.sort(key=sort_key)
    return list


if __name__ == "__main__":
    print (sort_by_third([('abc', 'bcd'), ('abc', 'zza')]))
