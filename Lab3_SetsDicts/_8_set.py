
def return_elements(inputset):
    """Sa se scrie o functie care primeste ca parametru un set.

    Returneaza un tuplu (a, b).
    A reprezentand numarul de elemente unice din set.
    B reprezentand numarul de elemente duplicate din set.
    """
    return len(inputset), 0


if __name__ == "__main__":
    print return_elements(set([1, 2, 3, 4, 4, 4, 4, 5, 6]))
