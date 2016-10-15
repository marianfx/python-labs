
def polinom(pol, value):
    """Se da un sir de caractere care reprezinta un polinom.

    (Ex: "3x^3 + 5x^2 - 2x - 5") si un numar (intreg sau float).
    Sa se evalueze polinomul respectiv pentru valoarea data.
    """
    pol = pol.lower()
    newstr = ""
    i = 0
    for c in pol:
        if c == "x":
            if i == 0:
                newstr += str(value)
            elif not pol[i - 1].isalnum():
                newstr += str(value)
            else:
                newstr += "*" + str(value)
        elif c == "^":
            newstr += "**"
        else:
            newstr += c
        i += 1
    result = eval(newstr)
    return result

if __name__ == "__main__":
    print (polinom("x^3 + 5x^2 - 2x - 5", 2))
