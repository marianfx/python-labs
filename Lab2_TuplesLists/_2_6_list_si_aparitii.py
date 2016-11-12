
from _2_4_doualiste import list_all_elements
from _2_4_doualiste import list_reunion


def x_in_lists(*args):
    """Sa se scrie o functie care primeste ca parametru

    un numar variabil de liste si un numar intreg x.
    Sa se returneze o lista care sa contina elementele care apar de exact x ori
    in listele primite. Exemplu:
    pentru listele [1,2,3], [2,3,4], [4,5,6], [4, 1, "test"] si x = 2
    se va returna [1, 2, 3]
    # 1 se afla in lista 1 si 4, 2 se afla in lista 1 si 2, 3 in 1 si 2.
    """
    lists = [list(x) for x in args[0:-1]]
    x = args[-1]
    all_elements = []
    distinct_elements = []

    for lst in lists:
        all_elements = list_all_elements(all_elements, lst)
        distinct_elements = list_reunion(distinct_elements, lst)

    output = []
    for element in distinct_elements:
        if all_elements.count(element) == x:
            output.append(element)
            pass
    output.sort()

    return output

if __name__ == "__main__":
    print (x_in_lists([1, 2, 3], [2, 3, 4], [4, 5, 6], [4, 1, "test"], 2))
