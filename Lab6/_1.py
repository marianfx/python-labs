
import re

WORDREGEX = r"(\w+)"
R = re.compile(WORDREGEX)

def extract_words(text):
    """Extracts the words from a text."""
    return R.findall(text)

if __name__ == "__main__":
    TEXT = "Marian is walking home t0day!"
    print(extract_words(TEXT))

