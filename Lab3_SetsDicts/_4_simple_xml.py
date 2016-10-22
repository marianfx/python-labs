
def build_xml(tag, content, **kArgs):
    """Fie functia build_xml_element care primeste urmatorii parametri:

    tag, content si elemente cheie-valoare date ca parametri cu nume.
    Sa se construiasca si sa se returneze un string,
    care reprezinta elementul XML aferent.
    Exemplu:
    build_xml_element("a", "Hello there",
                            href="http://python.org",
                            _class="my-link",
                            id="someid") =>
    "<a href=\"http://python.org\" _class=\"my-link\" id=\"someid\">
        Hello there
    </a>"
    """
    output = ""
    output += "<" + tag + " "
    for pair in kArgs.items():
        name = pair[0]
        val = pair[1]
        output += name + "=\"" + val + "\" "
    # remove space
    output = output[0:-1]
    output += ">\n" + content + "\n</" + tag + ">"
    return output

if __name__ == "__main__":
    print(build_xml("a", "Hello world!", href="http://python.org", _class="my-link", id="someid"))
