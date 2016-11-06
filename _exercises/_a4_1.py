
def numara_caractere(text, caractere):
    return sum([text.count(x) for x in caractere])


def gaseste_asemanatori(list1, list2):
    seen = set()
    seen_add = seen.add
    return [x for x in list1 if x in list2 and not (x in seen or seen_add(x))]


def rezolva_pattern(template, context):
    for key in context.keys():
        template = template.replace("#" + key + "#", context[key])
    return template


if __name__ == "__main__":
    # print(numara_caractere(text="Python is awesome", caractere=("o", "e")))
    # print(gaseste_asemanatori([1,2,3,4,5,6,5,4,3,2,1], [1,1,2,2,3,3,4,5]))
    print(rezolva_pattern(template="Dont {{do}} this #do#", context={"do": ", seriously"}))
