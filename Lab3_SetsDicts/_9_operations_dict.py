
def return_operations(*sets):
    """Sa se scrie o functie care primeste un numar variabil de seturi.

    Returneaza un dictionar cu urmatoarele operatii dintre toate seturile doua cate doua:
    reuniune, intersectie, a-b, b-a.
    Cheia va avea urmatoarea forma: "a op b".
    """
    output = {}
    for i in range(0, len(sets)):
        for j in range(i + 1, len(sets)):
            set1 = sets[i]
            set2 = sets[j]
            key = str(set1) + ' | ' + str(set2)
            value = set1 | set2
            output[key] = value
            key = str(set1) + ' & ' + str(set2)
            value = set1 & set2
            output[key] = value
            key = str(set1) + ' - ' + str(set2)
            value = set1 - set2
            output[key] = value
            key = str(set2) + ' - ' + str(set1)
            value = set2 - set1
            output[key] = value
    return output


if __name__ == "__main__":
    output = return_operations({1, 2, 3}, {3, 4, 5}, {5, 6, 7})
    for pair in output.items():
        print (pair)
