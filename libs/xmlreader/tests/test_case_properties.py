"""
    junit test case properties
"""
from libs.xmlreader.xmlreader.cases import Cases
from libs.xmlreader.xmlreader.junitxml import XmlFileParser
from libs.xmlreader.xmlreader.properties import Properties
from libs.xmlreader.xmlreader.suites import Suites


def test_properties(record_property):
    record_property('Test Case', '')

    suites = Suites(XmlFileParser('./data/output.xml').xml_doc)

    while suites.next():
        cases = Cases(suites.get_current())

        for case in cases.get_all():
            properties = Properties(case)

            while properties.next():
                print(properties.get_current().getAttribute('name'))
