
def transformer(text):
    """Scrieti o functie care converteste in sir de caractere.

    Convertire din UpperCamelCase in lowercase_with_underscores.
    """
    out = ""
    for c in text:
        if c.isupper() and out == "":
            out += c.lower()
        elif c.isupper and not out[-1].isalnum():
            out += c.lower()
        elif c.isupper() and out != "":
            out += "_" + c.lower()
        else:
            out += c
    return out

if __name__ == "__main__":
    print (transformer("Upper CamelCase "))
