import sys


def sumacifre(n):
    if n // 10 == 0:
        return n
    return n % 10 + sumacifre(n // 10)


def mcifre(suma, n):
    count = 0
    nr = 0
    output = []
    while count < n:
        if sumacifre(nr) == suma:
            output.append(nr)
            count += 1
        nr += 1
    return output


def caractere(text1, text2):
    set1 = set(text1)
    set2 = set(text2)
    return set1.intersection(set2)


def cuvinte(text):
    return {cuvant: text.lower().split().count(cuvant) for cuvant in text.lower().split()}

if __name__ == "__main__":
    # 1 print(mcifre(0, 1))
    # 2 print(caractere("abcde", "abc"))
    print(cuvinte("ana are Mere mere"))
