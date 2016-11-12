
visited = []
indexes = []


def combinari(k, len, max, list, output):
    """Idee: generez combinari pe indecsi (1..n) si afisez din lista[i]."""
    global visited
    global indexes

    if k - 1 == max:
        temp_list = []
        for i in range(1, max + 1):
            temp_list.append(list[indexes[i] - 1])
        output.append(tuple(temp_list))
        return output

    for i in range(1, len + 1):
        if visited[i] == 0 and indexes[k - 1] < i:
            indexes[k] = i
            visited[i] = 1
            combinari(k + 1, len, max, list, output)
            visited[i] = 0

    return output


def combinarink(list, k):
    """Sa se scrie o functie care primeste ca parametru o lista x si un numar k.

    Sa se returneze o lista cu tuple care sa reprezinte combinari
    de len(x) luate cate k din lista x.
    Exemplu: pentru lista x = [1,2,3,4] si k = 3
    se va returna [(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)].
    """
    global visited
    global indexes
    visited = [0 for x in range(0, len(list) + 1)]  # init with 0
    indexes = [x for x in range(0, len(list) + 1)]  # init indexes with 0...n-1
    output = combinari(1, len(list), k, list, [])
    print (output)

if __name__ == "__main__":
    combinarink([1, 2, 3, 4], 3)
