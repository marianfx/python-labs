
import re

def getFileContent(path):
    fopen = open(path)
    text = fopen.read()
    fopen.close()
    return text


def parsexmlrecursively(xml, regex, innergroupindex):
    """Given an xml string and a regex to match elements for, searches matches recursively.

    :param innergroupindex: Should be the index of the group (from the regex)
                            that identifies the group containing the inner element.
                            Ex regex: <elem attrsregex>(innerregex)</elem>
                                This one has only one group, so index will be 1.
    """
    reg = re.compile(regex)
    spacereg = re.compile(r" +(<\/\w+>)$")

    output = []
    searchqueue = [xml]
    while True:
        if len(searchqueue) == 0:
            break
        text = searchqueue.pop()
        results = reg.findall(text) # get a list with all the matches for the current text
        for result in results:
            length = len(result)
            if length < 1:
                continue
            text = spacereg.sub(r'\1', result[0])
            output.append(text) # first element is the whole element matched
            if length < 2:
                continue
            # add the inner possible text to search for matches
            searchqueue.append(result[innergroupindex])
    return output


def xmlparse(xmlpath, attrs):
    """Loads the xml file into a string and gets the elements matching attrs.

    Details: attrs contains attributes (xml-style) that an element must contain.
    Regex will match elements containing these attributes in ANY ORDER
    (uses lookaheads).
    """
    xml = getFileContent(xmlpath)
    # normalize ' => "
    xml = xml.replace("'", "\"")

    # build the regex; \2 means start and end with the same word
    regex = r"(<(\w+).*(@_attributes).*>((.|\n)*?)<\/\2>)"

    # use | to match at least one of them
    keyvalueoutput = [key + "=\"" + value + "\"" for (key, value) in attrs.items()]
    atleastone = "|".join(keyvalueoutput)
    regex = regex.replace("@_attributes", atleastone)

    print("The search regex is:\n" + regex)

    # search recursively for inner elements; see test.xml for example
    return parsexmlrecursively(xml, regex, 3)

DICT = {
    "class": "url",
    "name": "url-form",
    "data-id": "item",
    "test": "nothing"
}

if __name__ == "__main__":
    OUTPUT = xmlparse("./Lab6/test.xml", DICT)
    print("Output:")
    for element in OUTPUT:
        print(element)
