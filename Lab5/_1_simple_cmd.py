import sys
# First parameter is always the file name.
if __name__ == "__main__":
    try:
        if len(sys.argv) < 3:
            raise Exception("Need at least 2 parameters.")
        a = int(sys.argv[1])
        b = int(sys.argv[2])
        print(a - b, a + b, a / b, a * b)
    except Exception as captured:
        print(captured)
