
def count_chars(text):
    """Scrieti o functie care primeste ca parametru un sir de caractere.

    Returneaza un dictionar in care cheile sunt caracterele dn componenta sirului de caractere,
    iar valorile sunt reprezentate de numarul de aparitii ale caracterului in text.
    Exemplu: Pentru sirul "Ana are mere.":
    {'A': 1, ' ': 2, 'n': 1, 'a': 2, 'r': 2, 'e': 3, 'm': 1, '.': 1}.
    """
    uniquechars = set(text)
    output = {}
    for char in uniquechars:
        output[char] = text.count(char)
    return output

if __name__ == "__main__":
    print (count_chars("Ana are mere."))
