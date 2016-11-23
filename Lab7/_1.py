
from random import randint
import sys
import time

if __name__ == "__main__":
    args = sys.argv
    if len(args) < 3:
        raise Exception("One must provide 2 parameters a and b.")
    a = int(sys.argv[1])
    b = int(sys.argv[2])

    starttime = time.time()
    while True:
        nr = randint(a, b) # upper bound is inclusive
        time.sleep(nr)
        passed = time.time() - starttime
        passed = passed / 60.0
        print("%.2f" % passed)
