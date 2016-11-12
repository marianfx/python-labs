
import setops as so


if __name__ == "__main__":
    set1 = {1, 2, 3, 4}
    set2 = {4, 5, 6}
    print(so.reunion(set1, set2))
    print(so.intersection(set1, set2))
    print(so.minus(set1, set2))
    print(so.minus(set2, set1))
