from xml.dom.minidom import Element


class Properties:

    def __init__(self, testcase: Element):
        self.__properties_tag_name = 'property'
        self.__properties_iter = iter(testcase.getElementsByTagName(self.__properties_tag_name))
        self.__current = None

        print(f"INFO: Successfully extracted properties from test case")

    def next(self):
        next_value, self.__current = self.__next_iter_value(self.__properties_iter)
        return next_value

    def get_current(self):
        return self.__current

    @staticmethod
    def __next_iter_value(iter_list):
        try:
            return True, iter_list.__next__()
        except StopIteration:
            print(f"INFO: No more properties found")
            return False, None
