"""Client that connects to an URL and downloads images from the site or displays informations."""
import hashlib
import os
import re
from selenium import webdriver
import sys
import time
import urllib

URL = "https://www.instagram.com/fxmarian/"
REGEX = re.compile(rb"<li><a href=\"([^\"]+)\">(\1)</a></li>")
TXTREGEX = re.compile(r"^([^\.]+)\.txt$")
IMGREGEX = re.compile(r"<img(.|\n)+?src=\"([^\"]+)\"")
RMVFIRSTFLG = re.compile(r"(\/s(\d+)x\2)")
RMVSCNDFLG = re.compile(r"(\/c\d+\..+?)\/")
NAMEREGEX = re.compile(r".+\/(\w.+?(\.jpg|\.png|\.jpeg|\.gif|\.mp4))(?:\?)?")
GLBL_COUNTER = 0
BUFFERSIZE = 1000

def executetimed(func):
    """Executes a function and times it."""
    starttime = time.time()
    func()
    seconds = time.time() - starttime
    logger = open("logger.txt", "a")
    logger.write("Time passed: %.10f" % seconds)
    logger.close()

def get_response_hash(response, hasher=hashlib.md5()):
    """Hashes a string (profided hash mode) with buffersize."""
    fragments = []
    try:
        while True:
            chunk = response.read(BUFFERSIZE)
            if not chunk or len(chunk) == 0:
                break
            hasher.update(chunk)
            fragments.append(hasher.hexdigest())
        return fragments
    except:
        return ""

def get_response_info(url: str):
    """Given an responses stream, hashes it's contents (buffered)."""
    try:
        response = urllib.request.urlopen(url)
        status = response.status
        msg = response.msg
        length = response.headers['content-length']
        hashes = get_response_hash(response)

        logger = open("logger.txt", "w")
        logger.write("Status:\n---------------\n{0}:{1}\n\n".format(status, msg))
        logger.write("Length:\n---------------\n{0}\n\n".format(str(length)))
        logger.write("Hashes:\n---------------\n")
        for has in hashes:
            logger.write("{0}\n".format(has))
        logger.write("\n\n")
        logger.close()
    except Exception as exc:
        print("Error: {0}.\n".format(str(exc)))

def parse_insta_original_pics(pfile: str):
    """Removes instagram resizers.

    Removes things like "/s640x640" and "/c135.0.810.810"
    """
    pfile2 = str(pfile)
    first = RMVFIRSTFLG.search(pfile)
    if first:
        pfile2 = pfile.replace(first.group(1), "")
    second = RMVSCNDFLG.search(pfile2)
    if second:
        pfile2 = pfile2.replace(second.group(1), "")
    return pfile2

def download_image(url: str):
    """Downloads an image from the given url, using count naming format."""
    try:
        global GLBL_COUNTER
        GLBL_COUNTER += 1
        ext = NAMEREGEX.search(url).group(2)
        name = str(GLBL_COUNTER) + ext
        print("Parsing img {0} as {1}.\n".format(url, name))
        if not os.path.isdir("images"):
            os.mkdir("images")
        req = urllib.request.Request(
            url,
            data=None,
            headers={
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
            }
        )
        response = urllib.request.urlopen(req).read()
        filepath = os.path.join("images", name)
        writer = open(filepath, "wb")
        writer.write(response)
        writer.flush()
        writer.close()
    except Exception as e:
        print("Cannot download valid image from URL: " + url)
        print(str(e))

def download_url_images(url: str, insta_origin_feature=True):
    """Access a http server profiding directory listing, and print txts."""
    try:
        driver = webdriver.PhantomJS()
        driver.set_window_size(1024, 768)
        driver.get(url)
        response = driver.page_source

        reg_obs = IMGREGEX.findall(response)
        if len(reg_obs) == 0:
            print("No files to download.")
            return None

        imgs = []
        for entry in reg_obs:
            pfile = entry[1]
            if insta_origin_feature:
                pfile = parse_insta_original_pics(pfile)
            imgs.append(pfile)

        if len(imgs) == 0:
            print("No files to download.")
        for img in imgs:
            download_image(img)
    except Exception as exc:
        print("Error: {0}.\n".format(str(exc)))




if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("You must provide the mode (img/insta/info) and the url as arguments")
        exit(0)
    MODE = sys.argv[1]
    URL = sys.argv[2]
    if MODE == "info":
        EXECUTER = lambda: get_response_info(URL)
        executetimed(EXECUTER)
    elif MODE == "img":
        download_url_images(URL, False)
    elif MODE == "insta":
        download_url_images(URL)
    else:
        print("Cannot identify what you want (first arg is mode and can be img, insta or info).")
