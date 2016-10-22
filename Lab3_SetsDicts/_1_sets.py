
def list_operations(list1, list2):
    """Sa se scrie o functie care primeste ca parametri doua liste a si b.

    Returneaza un tuplu de seturi care sa contina: (a intersectat cu b, a reunit cu b, a - b, b - a).
    Se foloseste de operatiile pe seturi.
    """
    l1set = set(list1)
    l2set = set(list2)
    aminusb = l1set - l2set
    bminusa = l2set - l1set
    reunion = l1set | l2set
    intersect = l1set & l2set

    return intersect, reunion, aminusb, bminusa

if __name__ == "__main__":
    print (list_operations([1, 2, 3, 4], [3, 4, 5, 6]))
