import sys
import os

def go_recursive(path):
    """Go recursively through a directory."""
    print(path)
    if not os.path.isdir(path):
        return
    for entry in os.listdir(path):
        new_path = os.path.join(path, entry)
        go_recursive(new_path)

if __name__ == "__main__":
    try:
        if len(sys.argv) < 2:
            raise Exception("Need a path as parameter.")

        path = sys.argv[1]
        if not os.path.isdir(path):
            raise Exception("The given argument is not a path.")

        go_recursive(path)
    except Exception as captured:
        print(str(captured))
