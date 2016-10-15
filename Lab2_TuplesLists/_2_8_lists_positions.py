
def checker(lst):
    """Create a lambda function to return the element at a index or None"""
    return lambda index: lst[index] if index < len(lst) else None


def lists_positions(*lists):
    # step 1 = uniformizare
    # Obs: max() returneaza elementul maxim, nu lungimea lui. Doh.
    max_length = len(max(lists, key=lambda lst: len(lst)))

    # Creez o noua lista, mergand pe indecsi de la 0 la max_length
    # Daca indexul e in lista, pun elementul, daca nu pun None (checker)
    lists = map(lambda lista: map(checker(lista), range(0, max_length)), lists)

    # Apelex cu *lists pt. ca * face unpack la elementele din lista
    # adica il transfera intr-un apel de tipul zip(seq1, seq2, seq3, ...)
    return zip(*lists)


if __name__ == "__main__":
    print (lists_positions([1, 2], [5, 6, 7], ["a", "b", "c"]))
