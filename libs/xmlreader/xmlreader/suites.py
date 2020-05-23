import xml.dom.minidom


class Suites:

    def __init__(self, xmldoc: xml.dom.minidom.Document):

        self.__test_suite_tag_name = 'testsuite'

        self.all = xmldoc.getElementsByTagName(self.__test_suite_tag_name)

        self._iter = iter(self.all)

        self._current = None

        print(f'INFO: Successfully extracted test suites')

    def next(self):
        next_value, self._current = self.__next_iter_value(self._iter, 'suites')
        if not next_value:
            print(f"No more suites found")
        return next_value

    def get_current(self):
        return self._current

    @staticmethod
    def __next_iter_value(iter_list, item):
        try:
            return True, iter_list.__next__()
        except StopIteration:
            print(f"INFO: No more {item} found")
            return False, None
