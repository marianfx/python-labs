
from hashlib import sha256
import os
import time

BUFFERSIZE = 4096

def executetimed(func):
    starttime = time.time()
    func()
    seconds = time.time() - starttime
    print("Time passed: %.10f" % seconds)

def get_file_content_hash(path):
    try:
        sha = sha256()
        fread = open(path, 'rb')
        while True:
            chunk = fread.read(BUFFERSIZE)
            if len(chunk) == 0:
                break
            sha.update(chunk)
        fread.close()
        return sha.hexdigest()
    except:
        return ""

def findduplicates(path):
    if not os.path.isdir(path):
        raise Exception("The given path is not a directory.")

    filelist = list(filter(lambda fl: os.path.isfile(fl), os.listdir(path)))
    groups = []
    index = 0
    while len(filelist) != 0:
        file1 = filelist.pop()
        hash1 = get_file_content_hash(file1)
        groups.append([file1])
        i = 0
        while len(filelist) != 0 and i < len(filelist):
            file2 = filelist[i]
            hash2 = get_file_content_hash(file2)
            if hash1 == hash2:
                groups[index].append(file2)
                del filelist[i]
            i += 1
        index += 1
    # write file
    fwrite = open('output.txt', 'w')
    fwrite.write("Groups of files are separated by multi-line.\n\n")
    for group in groups:
        for path in group:
            fwrite.write(path + "\n")
        fwrite.write("\n")
    fwrite.flush()
    fwrite.close()

if __name__ == "__main__":
    EXECUTER = lambda: findduplicates(".")
    executetimed(EXECUTER)
