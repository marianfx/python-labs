import sys
import os


def process_dir(writer, root, directory):
    full_dirName = os.path.join(root, directory)
    writer.write(full_dirName + "|")
    if os.path.isdir(full_dirName):
        writer.write("DIRECTORY")
    else:
        writer.write("UNKNOWN")
    writer.write("\n")


def process_file(writer, root, fileName):
    full_fileName = os.path.join(root, fileName)
    writer.write(full_fileName + "|")
    if os.path.isfile(full_fileName):
        writer.write("FILE")
    else:
        writer.write("UNKNOWN")
    writer.write("\n")


if __name__ == "__main__":
    try:
        if len(sys.argv) < 3:
            raise Exception("Need a directory path and a file as parameter.")

        path = sys.argv[1]
        f = sys.argv[2]
        writer = open(f, 'w')
        if not os.path.isdir(path):
            raise Exception("The given argument is not a path.")

        for (root, directories, files) in os.walk(path):
            for directory in directories:
                process_dir(writer, root, directory)
            for fileName in files:
                process_file(writer, root, fileName)
        writer.flush()
        writer.close()
    except Exception as captured:
        print(str(captured))
