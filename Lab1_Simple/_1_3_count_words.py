
def nrWords(text):
    """Scrieti o functie care returneaza numarul de cuvinte din string.

    Cuvintele sunt separate de spatii, semne de punctuatie (, ;, ? ! . ).
    """
    list = text.replace(',', ' ').replace('.', ' ').replace(';', ' ')
    list = list.replace('!', ' ').replace('?', ' ').split()

    return len(list)

if __name__ == "__main__":
    print (nrWords("Marian,Focsa     tare"))
