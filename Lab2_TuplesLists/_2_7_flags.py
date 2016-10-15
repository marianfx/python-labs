
def flags(x=1, flag=True, *strings):
    """Sa se scrie o functie care primeste ca parametri

    un numar x default egal cu 1, un numar variabil de siruri de caractere,
    si un flag boolean setat default pe True.
    Pentru fiecare sir de caractere, sa se genereze o lista care sa contina
    caracterele care au codul ASCII divizibil cu x, daca flag-ul e pe True.
    In caz contrar sa contina caracterele care au codul ASCII nedivizibil cu x.
    Exemplu:
    x=2, "test", "hello", "lab002", flag=False
    va returna (["e", "s"], ["e", "o"], ["a"]).
    Atentie:
    functia trebuie sa returneze un numar variabil de liste care sa corespunda
    cu numarul de siruri de caractere primite ca input.
    """
    output = []
    for string in strings:
        temp_list = []
        for char in string:
            if flag is True and ord(char) % x == 0:
                    temp_list.append(char)
            elif flag is False and ord(char) % x != 0:
                    temp_list.append(char)
        output.append(temp_list)

    return tuple(output)


if __name__ == "__main__":
    print (flags(2, False, "test", "hello", "lab002"))
