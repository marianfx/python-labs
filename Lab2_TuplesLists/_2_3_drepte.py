
def getEq(A, B):
    if A[1] == B[1]:  # cazul ya = yb (dreapta orizontala)
        return 0, 1, -B[1]
    if A[0] == B[0]:  # cazul xa = xb (dreapta verticala)
        return 1, 0, -A[0]

    # other cases: a = Ya - Yb, b = Xb - Xa, c = Xa * Yb - Xb * Ya
    a = A[1] - B[1]
    b = B[0] - A[0]
    c = A[0] * B[1] - B[0] * A[1]
    return a, b, c


def parsePoints(points):
    """Fie un tuplu (x,y) reprezentarea unui punct intr-un sistem cartezian.

    Sa se scrie o functie care primeste ca parametru o lista de puncte
    si returneaza o lista de tuple (a,b,c) unice care reprezinta dreptele unice
    determinate de acele puncte ( (a,b,c) corespunde dreptei ax + by + c = 0).
    """
    i = 0
    n = len(points)
    list = []
    for point in points:
        for j in range(i + 1, n):
            list.append(getEq(point, points[j]))
    return list

if __name__ == "__main__":
    print (parsePoints([(1, 3), (3, 7), (1, 1)]))
