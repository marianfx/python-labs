

import json
import os
import sys
import time
import zipfile


def deserialize(path):
    return json.loads(open(path, 'rt').read())


if __name__ == "__main__":
    #if len(sys.argv) < 2:
    #    raise Exception("Must provide path to json")
    
    dictio = deserialize(sys.argv[1])
    zzip = zipfile.ZipFile("arhiva.zip", "w", zipfile.ZIP_DEFLATED)

    for key in dictio.keys():
        sizeb = dictio[key]["size_fisier"]
        fullpath = dictio[key]["cale_absoluta"]
        currenttime = time.time()
        lastmtime = os.path.getmtime(fullpath)
        if (currenttime - lastmtime) <= 5000:
            continue
        zzip.write(key)

