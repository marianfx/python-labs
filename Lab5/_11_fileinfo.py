
import os

def det_file_info(path):
    if not os.path.isfile(path):
        raise ValueError("Path should be a file.")
    fullpath = os.path.abspath(path)
    filesize = os.path.getsize(path)
    file_extension = os.path.splitext(path)[1]
    can_read = True
    can_write = True
    try:
        fread = open(path, 'r')
    except IOError:
        can_read = False
    try:
        fwrite = open(path, 'a')
    except IOError:
        can_write = False

    return{
        "full_path": fullpath,
        "file_size": filesize,
        "file_extension": file_extension,
        "can_read": can_read,
        "can_write": can_write
        }


if __name__ == "__main__":
    result = det_file_info('path')
    print(result)
