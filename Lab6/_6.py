
import re


def cenzura(text):
    """Replaces in text, for words s / e with vowels, the odd positions with *."""
    words = r"(\W|^)([aeiou]\w+[aeiou])" #Finds out words s / e with vowels
    odds = r"(\w)(\w)|(\w)" # Finds groups of positions (impar, par)
    wwregex = re.compile(words, flags=re.IGNORECASE)
    oddregex = re.compile(odds, flags=re.IGNORECASE)

    alll = wwregex.findall(text)
    vector = [y for (x, y) in alll]
    for www in vector:
        neww = oddregex.sub('*\\2', www)
        print(neww)
        text = wwregex.sub(r"\1" + neww, text, count=1)
    return text

if __name__ == "__main__":
    print(cenzura("Andreea este tare!"))

