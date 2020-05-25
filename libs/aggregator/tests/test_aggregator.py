import pytest

from libs.aggregator.aggregator.aggregator import Aggregator
from libs.xmlreader.xmlreader.cases import Cases
from libs.xmlreader.xmlreader.junitxml import XmlFileParser
from libs.xmlreader.xmlreader.suites import Suites


def case_builder(suites):
    cases = []
    while suites.next():
        cases += Cases(suites.get_current()).get_all()

    return cases


@pytest.mark.parametrize('filename', ['./data/output.xml'])
def test_aggregator(filename):
    junit_xml = XmlFileParser(filename)
    suites = Suites(junit_xml.xml_doc)

    cases = case_builder(suites)

    aggregator = Aggregator()

    aggregator.case_states_aggregation(cases)

    tmp = aggregator.get_aggregated_result()
    for id in tmp:
        print(id, tmp[id].count, tmp[id].passes, tmp[id].error, tmp[id].fails, tmp[id].skip, tmp[id].warn,
              tmp[id].passes/tmp[id].count > tmp[id].threshold)

