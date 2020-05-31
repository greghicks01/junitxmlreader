"""
 testsuites with one and two elements
"""

import pytest
from xml.dom.minidom import Element
from libs.xmlreader.xmlreader.junitxml import XmlFileParser
from libs.xmlreader.xmlreader.suites import Suites


@pytest.mark.parametrize('filename,expected_count', [('./data/output.xml', 1), ('./data/multisuite.xml', 2)])
def test_suite_count(filename, expected_count, record_property):
    record_property('Test Case', '')

    junit_xml = XmlFileParser(filename)

    suites = Suites(junit_xml.xml_doc)

    assert suites is not None

    suite_count = 0
    while suites.next():
        suite_count += 1

    assert suite_count == expected_count


def test_suite():

    junit_xml = XmlFileParser('./data/output.xml')

    suites = Suites(junit_xml.xml_doc)

    suites.next()

    assert type(suites.get_current()) is Element
