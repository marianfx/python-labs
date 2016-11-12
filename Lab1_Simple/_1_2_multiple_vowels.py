
def nrvocale(text):
    """Scrieti o functie care calculeaza cate vocale sunt intr-un string"""
    count = 0
    for c in text:
        if c in ['a', 'e', 'i', 'o', 'u']:
            count = count + 1
    return count

if __name__ == "__main__":
    print (nrvocale("Marian"))
