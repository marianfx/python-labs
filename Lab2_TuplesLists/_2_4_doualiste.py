
def list_intersect(list1, list2):
    """Given two lists, A and B, returns A intersect B."""
    return filter(lambda x: x in list2, list1)


def list_all_elements(list1, list2):
    """Given two lists, A and B, returns A extended by B."""
    return list1 + list2


def list_reunion(list1, list2):
    """Given two lists, A and B, returns A reunion B."""
    return list(set(list1) | set(list2))


def list_a_minus_b(list1, list2):
    """Given two lists, A and B, returns A-B."""
    return filter(lambda x: x not in list2, list1)


def list_b_minus_a(list1, list2):
    """Given two lists, A and B, returns B-A."""
    return filter(lambda x: x not in list1, list2)


def doualiste(list1, list2):
    """Sa se scrie o functie care primeste ca parametri doua liste,a si b.

    Returneaza: (a intersectat cu b, a reunit cu b, a - b, b - a).
    """
    intersect = list_intersect(list1, list2)
    reunion = list_reunion(list1, list2)
    aminusb = list_a_minus_b(list1, list2)
    bminusa = list_b_minus_a(list1, list2)

    return intersect, reunion, aminusb, bminusa

if __name__ == "__main__":
    print (doualiste([1, 2, 3, 4, 5, 6], [4, 5, 6, 7, 8, 9, 10]))
