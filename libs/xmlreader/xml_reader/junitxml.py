import os
import xml.dom.minidom as xml


class XmlFileParser:

    def __init__(self, filename: str):

        if os.path.isfile(filename):
            self.xml_doc: xml = xml.parse(filename)
            print(f"Successfully opened {filename}")
        else:
            raise FileNotFoundError(f"Can't find {filename}")
