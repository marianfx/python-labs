import sys
import os

if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            raise Exception("Need a path as parameter.")
        path = sys.argv[1]
        theFile = open(path, 'w')
        for pair in os.environ.items():
            theFile.write(pair[0] + "\t" + pair[1] + "\n")
        theFile.flush()
        theFile.close()
    except Exception as captured:
        print(str(captured))
