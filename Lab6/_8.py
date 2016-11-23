
import re
import os

REGEX = ""
REG = None
NAMEREG = None

def getfiledescriptor(fisier):
    filename = os.path.basename(fisier)

    if NAMEREG.match(filename) is None:
        return 0

    contents = open(fisier).read()
    if REG.search(contents):
        return 2
    # test x = "_3"
    return 1

def gorecurs(path):
    if os.path.isfile(path):
        typo = getfiledescriptor(path)
        if typo == 2:
            print(">>" + path)
        elif typo == 1:
            print(">" + path)
        return
    if not os.path.isdir(path):
        return

    for entry in os.listdir(path):
        newpath = os.path.join(path, entry)
        gorecurs(newpath)


if __name__ == "__main__":
    REGEX = r"_\d"
    REG = re.compile(REGEX)
    NAMEREG = re.compile(REGEX + r"(\.\w+)?$")
    gorecurs(".")

