from libs.xmlreader.xmlreader.case_state import States
from libs.xmlreader.xmlreader.cases import Cases
from libs.xmlreader.xmlreader.junitxml import XmlFileParser
from libs.xmlreader.xmlreader.properties import Properties
from libs.xmlreader.xmlreader.suites import Suites


def case_builder(suites):
    cases = []
    while suites.next():
        cases += Cases(suites.get_current()).get_all()

    return cases


def get_test_case_id_property(case):

    properties = Properties(case)
    while properties.next():
        if properties.get_current().getAttribute('name') == 'Test Case':
            print(f"INFO: Test case = {properties.get_current().getAttribute('value')}")
            return properties.get_current().getAttribute('value')

    return ''


def get_case_states(case):

    states = States(case)

    error = False
    fail = False
    skip = False
    warn = False

    if states.next_error():
        error = True

    if states.next_fail():
        fail = True

    if states.next_skip():
        skip = True

    if states.next_warn():
        warn = True

    return error, fail, skip, warn


def test_states(record_property):
    record_property('Test Case', '')

    suites = Suites(XmlFileParser('./data/multisuite.xml').xml_doc)
    cases = case_builder(suites)

    for case in cases:
        print('INFO: Analysing next test case')
        test_case_id = get_test_case_id_property(case)
        error, fail, warn, skip = get_case_states(case)

        print('INFO: end test case analyse')
