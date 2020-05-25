from xml.dom.minidom import Element

from libs.aggregator.aggregator.casestates import StateCount
from libs.xmlreader.xmlreader.case_state import States
from libs.xmlreader.xmlreader.properties import Properties


class Aggregator:

    def __init__(self):
        self.__no_case_id = 'untraceable'
        self.results = {self.__no_case_id: StateCount(1.0)}
        self.results_iter = None
        self.__current = None
        
    def case_states_aggregation(self, cases):

        for case in cases:
            case_id = self.get_case_id(case)

            if case_id != '':
                if case_id not in self.results:
                    self.results[case_id] = StateCount(1.0)

            error, fail, skip, warn = self.get_case_states(case)
            self.results[case_id].update(error, fail, skip, warn)

    def get_aggregated_result(self):
        return self.results

    @staticmethod
    def __next_iter_value(iter_list, item):
        try:
            return True, iter_list.__next__()
        except StopIteration:
            print(f"INFO: No more {item} found")
            return False, None

    def get_case_id(self, case: Element):
        properties = Properties(case)
        while properties.next():
            if properties.get_current().getAttribute('name') == 'Test Case':
                return properties.get_current().getAttribute('value')

        return self.__no_case_id

    @staticmethod
    def get_case_states(case: Element):

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
