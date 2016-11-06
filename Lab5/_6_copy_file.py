
import sys
import os

def copy_file_buffered(filePath, newPath, bufferSize):
    # copy
    freader = open(filePath, 'r')
    fwriter = open(newPath, 'w')
    while True:
        content = freader.read(bufferSize)
        fwriter.write(content)
        if content == "":
            break

    # close
    fwriter.flush()
    freader.close()
    fwriter.close()

if __name__ == "__main__":
    try:
        if len(sys.argv) < 4:
            raise Exception("Need three parameters.")

        filePath = sys.argv[2]
        dirPath = sys.argv[1]
        bufferSize = int(sys.argv[3])

        # tests
        if not os.path.isdir(dirPath):
            raise Exception("The first argument must be a path to an existing directory.")
        if not os.path.isfile(filePath):
            raise Exception("The second argument must be a path to an existing file.")

        # build new Path
        fileName = os.path.basename(filePath)
        newPath = os.path.join(dirPath, fileName)
        if os.path.isfile(newPath):
            answer = input("The file already exists in the given directory? Enter 'y' to overwrite.")
            if answer.lower() != "y":
                exit()
            # treat same file case
            filePath = os.path.abspath(filePath)
            newPath = os.path.abspath(newPath)
            if filePath == newPath:
                exit()

        # execute copy
        copy_file_buffered(filePath, newPath, bufferSize)

    except Exception as captured:
        print(str(captured))
