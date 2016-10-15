
def containsSPecials(text):
    """Scrieti o functie care verifica daca un sir de caractere contine>

    caractere speciale (\r, \t, \n, \a, \b, \f, \v).
    """
    for c in text:
        if c in ['\r', '\t', '\n', '\a', '\b', '\f', '\v']:
            return True
    return False

if __name__ == "__main__":
    print (containsSPecials("Marian"))
