
import sys
import os

def create_dummies(parentpath, depth):
    global filesize; global filecount; global dircount; global maxdepth;
    
    # write files
    for fcount in range(0, filecount):
        filename = os.path.join(parentpath, "file" + str(fcount))
        fwrite = open(filename, 'w')
        fwrite.write('a' * filesize)
        fwrite.flush()
        fwrite.close()
    
    if depth == maxdepth:
        return
    
    for dcount in range(0, dircount):
        dirname = os.path.join(parentpath, "dir" + str(dcount))
        try:
            os.makedirs(dirname)
        except OSError:
            print("Directory already exists.")
        else:
            create_dummies(dirname, depth + 1)


if __name__ == "__main__":
    if len(sys.argv) < 6:
        raise Exception("Need 5 parameters.")
    path = sys.argv[1]
    maxdepth = int(sys.argv[2])
    filesize = int(sys.argv[3])
    filecount = int(sys.argv[4])
    dircount = int(sys.argv[5])
    create_dummies(path, 1)
