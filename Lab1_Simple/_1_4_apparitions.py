
def countApp(text1, text2):
    """Scrieti o functie care primeste ca parametri doua siruri de caractere.

    Returneaza numarul de aparitii ale primului sir de caractere in al doilea.
    """
    return text2.lower().count(text1.lower())

if __name__ == "__main__":
    print (countApp("mA", "Marian"))
