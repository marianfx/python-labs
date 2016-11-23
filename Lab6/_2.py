
import re

def maxxmatches(regex, text, x):
    """Returns the substrings of length x from text, matching regex."""
    reg = re.compile(regex)
    result = reg.findall(text)
    return list(filter(lambda string: len(string) <= x, result))


if __name__ == "__main__":
    TEXT = "Ana has apples."
    REGEX = r"(\w+)"
    print(maxxmatches(REGEX, TEXT, 3))
