"""
    junit test cases
"""
from xml.dom.minidom import Element


class Cases:

    def __init__(self, testsuite: Element):

        self.__test_case_tag_name = 'testcase'

        self.all = testsuite.getElementsByTagName(self.__test_case_tag_name)

        print(f'INFO: Successfully extracted test cases in test suite')

    def get_all(self):
        return self.all
