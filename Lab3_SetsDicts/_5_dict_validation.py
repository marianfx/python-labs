
def validate_dict(rulez, dictionary):
    """Fie functia validate_dict.

    Primeste ca parametru un set de tuple care reprezinta reguli de validare
    pentru un dictionar cu chei de tipul string si valori tot de tipul string.
    Ultimul parametru primit este un dictionar.
    O regula este definita astfel: (cheie, "prefix", "middle", "sufix").
    O valoare este considerata valida daca:
        - incepe cu "prefix"
        - "middle" se gaseste in interiorul valorii (nu la inceput sau sfarsit)
        - se sfarsete cu "sufix".
    Functia va returna True daca dictionarul respecta toate regulile.
    Exemplu:
        - regulile:
            - [("key1", "", "inside", "")
            - ("key2", "start", "middle", "winter")]
        - dictionarul:
            {"key2": "starting the engine in the middle of the winter",
            "key1": "come inside, it's too cold outside",
            "key3": "this is not valid"}
        - Returneaza:
            - False (regulile sunt respectate pentru "key1" si "key2",
            dar apare "key3" care nu apare in reguli).

    """
    # Check for keyz
    keys_in_rulez = [x[0] for x in rulez]
    for key in dictionary.keys():
        if key not in keys_in_rulez:
            print("Failed: key \"" + key + "\" not in rulez.")
            return False

    for rule in rulez:
        key = rule[0]
        prefix = rule[1]
        middle = rule[2]
        suffix = rule[3]
        valtocheck = dictionary[key]
        if not valtocheck.startswith(prefix):
            print("Failed (prefix) at key:" + key)
            return False
        if middle not in valtocheck[1:-1]:
            print("Failed (middle) at key:" + key)
            return False
        if not valtocheck.endswith(suffix):
            print("Failed (suffix) at key:" + key)
            return False
    return True


if __name__ == "__main__":
    validate_dict(
        [("key1", "", "inside", ""), ("key2", "start", "middle", "winter")],
        {
            "key2": "starting the engine in the middle of the winter",
            "key1": "come inside, it's too cold outside",
            "key3": "this is not valid"
        })
