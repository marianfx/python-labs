import sys
import os

if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            raise Exception("Need a path as parameter.")
        path = sys.argv[1]
        if os.path.isfile(path):
            theFile = open(path)
            content = theFile.read(4096)
            print(content)
        elif os.path.isdir(path):
            for entry in os.listdir(path):
                print(entry)
        else:
            raise Exception("Invalid path.")
    except Exception as captured:
        print(str(captured))
