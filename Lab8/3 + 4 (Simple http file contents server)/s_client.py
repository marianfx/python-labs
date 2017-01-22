"""Client that connects to the simplehttpserver (directory listing)."""
import re
import urllib
from urllib import request

URL = "http://127.0.0.1:6996"
REGEX = re.compile(rb"<li><a href=\"([^\"]+)\">(\1)</a></li>")
TXTREGEX = re.compile(r"^([^\.]+)\.txt$")

def access_url(url: str):
    """Access a http server profiding directory listing, and print txts."""
    try:
        response = urllib.request.urlopen(url).read()
        print("Response from server\n--------------------:\n {0}\n--------------------\n".format
              (
                  response
              ))
        reg_obs = REGEX.findall(response)
        if len(reg_obs) == 0:
            print("No files to display.")
            return None

        txts = []
        for entry in reg_obs:
            pfile = entry[0].decode("UTF-8")
            match = TXTREGEX.match(pfile)
            if match:
                txts.append(match.group(1))

        if len(txts) == 0:
            print("No files to display.")
        for txt in txts:
            print(txt)
    except Exception as exc:
        print("Error: {0}.\n".format(str(exc)))


if __name__ == "__main__":
    access_url(URL)
