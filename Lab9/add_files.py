"""Script that adds file to database"""
import hashlib
import os
import sqlite3
import sys

CONN = sqlite3.connect("fileinfo.db")
LOCTABLE = """CREATE TABLE locatie
                            (id_locatie INTEGER PRIMARY KEY, locatie TEXT)"""
FTABLE = """CREATE TABLE files
                            (id_file INTEGER, id_locatie INTEGER)"""
ITABLE = """CREATE TABLE file_info
                            (id_file INTEGER PRIMARY KEY, nume_fisier TEXT, size_fisier INTEGER,
                            creation_time text, md5_pe_continut text)"""

def create_tables(path):
    """Creates the needed tables in the database."""
    conn = CONN.cursor()
    conn.execute(LOCTABLE)
    conn.execute(FTABLE)
    conn.execute(ITABLE)

    pathrowid = insert_into_loc(conn, path)
    for fl in os.listdir(path):
        newpath = os.path.join(path, fl)
        insert_into_files(conn, newpath, pathrowid)


def insert_into_loc(conn, path):
    strng = "INSERT INTO locatie VALUES (NULL, '" + path + "')"
    conn.execute(strng)
    return conn.lastrowid

def get_file_content_hash(path, sha):
    try:
        fread = open(path, 'rb')
        while True:
            chunk = fread.read(1024)
            if len(chunk) == 0:
                break
            sha.update(chunk)
        fread.close()
        return sha.hexdigest()
    except:
        return ""

def insert_into_files(conn, fl, pathrowid):
    name = os.path.basename(fl)
    size = os.path.getsize(fl)
    ctime = os.path.getctime(fl)
    chash = get_file_content_hash(fl, hashlib.md5())
    strng = "INSERT INTO file_info VALUES(NULL, '" + name + "', " + str(size) +", '" + str(ctime) + "', '" + chash + "')"
    conn.execute(strng)
    thisid = conn.lastrowid
    strng = "INSERT INTO files VALUES(" + str(thisid) + ", " + str(pathrowid) + ")"
    conn.execute(strng)

if __name__ == "__main__":
    DIRPATH = sys.argv[1]
    if not os.path.isdir(DIRPATH):
        exit(0)
    try:
        create_tables(DIRPATH)
    except:
        pass

    conn = CONN.cursor()
    query = """select * from locatie l
                            join files f on l.id_locatie = f.id_locatie
                            join file_info fi on fi.id_file = f.id_file
                            order by id_locatie"""
    for row in conn.execute(query):
        print(row)

    CONN.commit()
    CONN.close()
