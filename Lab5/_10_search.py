
import sys
import os

def search_recursively(list, target, to_search):
    if os.path.isfile(target):
        if to_search in open(target, 'r', errors="ignore").read():
            list.append(target)

    if os.path.isdir(target):
        subdirs = os.listdir(target)
        for subdir in subdirs:
            newpath = os.path.join(target, subdir)
            search_recursively(list, newpath, to_search)


def search_by_content(target, to_search):
    if not (os.path.isdir(target) or os.path.isfile(target)):
        raise ValueError("The 'target' argument must be a valid file or folder.")
    list = []
    search_recursively(list, target, to_search)
    print(list)


if __name__ == "__main__":
    search_by_content(".", "__name__")