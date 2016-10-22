
def compare_values(value1, value2):
    """ In-depth comparison of the two values.

    If the two are primitives, compare them directly.
    If the two are collections, go recursive through the elements.
    """
    print("Comparing " + str(value1) + " & " + str(value2) + ".")
    # if different types, sure not equal
    if type(value1) != type(value2):
        return False

    # check if they are containers or not
    try:
        n1 = len(value1)
        n2 = len(value2)
        # if length not equal, return False
        if n1 != n2:
            return False
        # else check for each pair
        for i in range(0, n1):
            val1 = value1[i]
            val2 = value2[i]
            if not compare_values(val1, val2):
                return False
    except:
        # if they are not containers, check for value equality
        if value1 != value2:
            return False

    # True if all comparisons are true
    return True


def compare_dicts(dict1, dict2):
    """Sa se compare doua dictionare fara a folosi operatorul "==".

    Sa se returneze un tuplu de liste de diferente astfel:
        (cheile_comune_dar_cu_valori_diferite,
        cheile_care_se_gasesc_doar_in_primul_dict,
        cheile_care_se_gasesc_doar_in_al_doilea_dict).
    Atentie:
        Dictionarele trebuiesc parcurse recursiv,
        deoarece la randul lor pot contine alte containere.
    """
    keys1 = set(dict1.keys())
    keys2 = set(dict2.keys())
    intersection = keys1 & keys2

    aminusb = keys1 - keys2
    bminusa = keys2 - keys1
    comm_but_diff = set()

    are_equal = False
    if intersection == keys1 | keys2:
        are_equal = True

    for key in intersection:
        print("Testing key " + key)
        values_are_equal = compare_values(dict1[key], dict2[key])
        if not values_are_equal:
            are_equal = False
            comm_but_diff.add(key)
    return (comm_but_diff, aminusb, bminusa, are_equal)

dict1 = {
            "1": [1, 2, 3, 4],
            "2": [1, 1, 1, 1],
            "3": 4,
            "5": {1, 2, 3, 4}
        }

dict2 = {
            "1": [1, 2, 3, 4],
            "2": [1, 1, 1, 2],
            "3": 4,
            "4": {1, 2, 3, 4}
        }

if __name__ == "__main__":
    print(compare_dicts(dict1, dict2))
