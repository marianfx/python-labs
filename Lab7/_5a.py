
import sys
import time
import _4 as four

if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Must provide dir argument.")
    while True:
        four.writejson(sys.argv[1])
        time.sleep(5 * 1000)

        