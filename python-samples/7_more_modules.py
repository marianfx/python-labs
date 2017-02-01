
##############
# TIME
#############
import time
seconds = time.time()
timetuple = time.ctime() # or time.localtime() or with seconds param
backtoseconds = time.mktime(timetuple)
string = time.strftime("%H %M %S %Y %m %B %d")


#############
# HASLIB
#############
import hashlib
hasher = hashlib.md5() # or sha256 etc
hasher.update(b"string") # requires list of bytes
output = hasher.hexdigest()

# Sample buffer-read and hash
import hashlib
def GetFileSHA1(filePath):
    try:
        m = hashlib.sha1()
        f = open(filePath,"rb")
        while True:
            data = f.read(4096)
            if len(data)==0: break
            m.update(data)
        f.close()
        return m.hexdigest()
    except:
        return ""


##############
# JSON & co
#############
import json # does serialization in 'text mode'
d = {"abc": 1}
# dump / load from string
stringjson = json.dumps(d)
backdict = json.loads(stringjson)
# dump / load from file
fobj = open("out.json", "wt")
json.dump(d, fobj)
fobj.close()
fobj = open("out.json", 'rt')
loaded = json.load(fobj)
print(loaded)

# PICKLE has the same options, but works binary (so wb/rb)
# MARSHAL does the same but is platform dependent


###########
# RANDOM
##########
import random
floatnr = random.random() # [0, 1)
intnr = random.randint(1, 2) # inclusive ambele capete
print(intnr)
lst = [1, 2, 3]
choice = random.choice(lst)
samplelist = random.sample(lst, 2) # chose random 2 members from lsst
random.shuffle(lst)


#############
# ZIPFILE
#############
import zipfile

# display files from arch
for entry in zipfile.ZipFile("path.zip").infolist():
    pass # eg entry.filename

# extract
zipfile.ZipFile("path").extract("path_from_arch", "dir_from_disk")

# open directly from zip
zfile = zipfile.ZipFile("path").open("path_inside_zip_o_file")
data = zfile.read()
zfile.close()
open("my_file", "wb").write(data)

# write in zip
zarch = zipfile.ZipFile("path")
zarch.write("path_to_file_inside_disk", "can_specify_path_in_arch") # adds it in the archive with the same path
zarch.close()