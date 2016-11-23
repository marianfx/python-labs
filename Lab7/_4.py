
import hashlib
import json
import os
import time

BUFFERSIZE = 4096

def get_file_content_hash(path, sha):
    try:
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

def getdataforfile(file):
    output = {}
    output["nume_fisier"] = os.path.basename(file)
    output["md5_fisier"] = get_file_content_hash(file, hashlib.md5())
    output["sha256_fisier"] = get_file_content_hash(file, hashlib.sha256())
    output["size_fisier"] = os.path.getsize(file)
    output["cand_a_fost_creat"] = time.strftime("%A, %B %Y - %H:%M:%S", time.localtime(os.path.getctime(file)))
    output["cand_a_fost_modificat"] = time.strftime("%A, %B %Y - %H:%M:%S", time.localtime(os.path.getmtime(file)))
    output["cale_absoluta"] = os.path.abspath(file)

    return output

def writejson(dirpath):
    filelist = list(filter(lambda fl: os.path.isfile(fl), os.listdir(dirpath)))
    bigdict = {}
    for fl in filelist:
        dictdata = getdataforfile(fl)
        bigdict[fl] = dictdata
    dumpstr = json.dumps(bigdict)
    open('serial.json', 'wt').write(dumpstr)

if __name__ == "__main__":
    writejson(".")
