import pytest

from libs.xmlreader.xmlreader.cases import Cases
from libs.xmlreader.xmlreader.junitxml import XmlFileParser
from libs.xmlreader.xmlreader.suites import Suites


@pytest.mark.parametrize('filename, expected_cases', [('./data/output.xml', 10), ('./data/multisuite.xml', 20)])
def test_cases_from_suite(filename, expected_cases, record_property):
    record_property('Test Case', '')

    suites = Suites(XmlFileParser(filename).xml_doc)
    assert suites is not None

    case_count = 0

    while suites.next():
        cases = Cases(suites.get_current())
        assert cases is not None

        for case in cases.get_all():
            case_count += 1

    assert case_count == expected_cases
