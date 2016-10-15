
def calafazan(char_len, *strings):
    """Scrieti o functie care>

     primeste un integer char_len si un numar variabil de stringuri.
     Verifica daca fiecare doua string-uri vecine respecta:
     al doilea string incepe cu ultimile char_len caractere a primului.
    """
    if len(strings) <= 1:
        return True
    a = strings[0]
    b = strings[1]
    x = a[-char_len:]
    y = b[0:char_len]
    if x != y:
        return False
    return calafazan(char_len, strings[1:])

if __name__ == "__main__":
    print (calafazan(2, "mare", "rema", "mare"))
