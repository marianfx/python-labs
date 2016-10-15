
def firstnfibbonaci(n):
    """Sa se scrie o functie care sa returneze o lista

    cu primele n numere din sirul lui Fibonacci.
    """
    count = 2
    list = []
    if (n > 0):
        list.append(0)
    if n > 1:
        list.append(1)

    while (count < n):
        list.append(list[count - 1] + list[count - 2])
        count += 1

    return list

if __name__ == "__main__":
    print (firstnfibbonaci(5))
