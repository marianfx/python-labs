
import random

def lotto():
    numbers = [(x + 1) for x in range(0, 69)]
    rr = random.Random()
    rr.shuffle(numbers) # shuffle the list
    output = []
    for i in range(0, 6):
        index = rr.randint(0, len(numbers) - 1)
        output.append(numbers.pop(index))
    return output


if __name__ == "__main__":
    print(lotto())
