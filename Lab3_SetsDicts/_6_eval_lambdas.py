
global_dict = {
        "+": lambda a, b: a + b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
        "%": lambda a, b: a % b
    }


def apply_operator(operator, a, b):
    """Sa se construiasca o functie apply_operator(operator, a, b).

    Functia va aplica peste a si b regula specificata de dictionarul global.
    Sa se implementeze astfel incat, in cazul adaugarii unui operator nou,
    sa nu fie necesara modificarea functiei.
    """
    func = global_dict[operator]
    return func(a, b)


if __name__ == "__main__":
    print(apply_operator("+", 2, 5))
