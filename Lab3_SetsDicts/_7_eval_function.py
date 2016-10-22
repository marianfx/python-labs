
global_dict = {
        "print_all": lambda *a, **k: print(a, k),
        "print_args_commas": lambda *a, **k: print(a, k, sep=", "),
        "print_only_args": lambda *a, **k: print(a),
        "print_only_kwargs": lambda *a, **k: print(k)
    }


def apply_function(operator, *a, **b):
    """Sa se construiasca o functie apply_operator(operator, a, b).

    Functia va aplica peste a si b regula specificata de dictionarul global.
    Sa se implementeze astfel incat, in cazul adaugarii unui operator nou,
    sa nu fie necesara modificarea functiei.
    """
    func = global_dict[operator]
    return func(*a, **b)


if __name__ == "__main__":
    apply_function("print_all", 2, 5, x1=2)
