"""
    junit_xml Tests
"""

import pytest
import xml.dom.minidom

from libs.xmlreader.xmlreader.junitxml import XmlFileParser


@pytest.mark.parametrize('filename', ['./data/output.xml', './data/multisuite.xml'])
def test_open_good_xml(filename, record_property):
    record_property('Test Case', '')

    junit_xml = XmlFileParser(filename)

    assert junit_xml is not None
    assert type(junit_xml) is XmlFileParser


@pytest.mark.parametrize('filename', ['./data/empty.xml', './data/malformed.xml'])
def test_open_bad_xml(filename):

    with pytest.raises(xml.parsers.expat.ExpatError):
        junit_xml = XmlFileParser(filename)



@pytest.mark.parametrize('filename', 'nonexistant.xml')
def test_open_filenotfound(filename):

    with pytest.raises(FileNotFoundError):
        junit_xml = XmlFileParser(filename)