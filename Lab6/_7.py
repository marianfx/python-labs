
import re


def iscnpvalid(text):
    sex = "([1-9])" # aparent Wikipedia spune ca exista 9 cifre
    year = "([0-9][0-9])" # orice an
    month = "((0[1-9])|(1[0-2]))" # lunile: 01 - 09, 10 - 12
    day = "((0[1-9])|([12][0-9])|(3[01]))" # zile: 01 - 09, 10 - 29, 30-31
    county = "((0[1-9])|([1-4][0-9])|(5[0-2]))" # judet: 01 - 09, 10 - 52
    nnn = r"(\d{3})" # trei cifre atribuite
    control = r"(\d)" # cifra de control
    cnp = sex + year + month + day + county + nnn + control + "$"
    if re.match(cnp, text) is None:
        return False
    return True


if __name__ == "__main__":
    print(iscnpvalid("1960804374545"))
