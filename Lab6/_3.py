
import re

def matchatleastone(text, regexes):
    """Returns a list of strings that match at least one of the regexes."""
    finalregex = "|".join(regexes)
    result = re.findall(finalregex, text)
    return result


if __name__ == "__main__":
    TEXT = "Welcome here, number 69!"
    REGEXES = [r"[a-zA-Z]+", r"mama"]
    print(matchatleastone(TEXT, REGEXES))
