from xml.dom.minidom import Element


class States:

    def __init__(self, case: Element):

        self.__error_state_tag_name = 'error'
        self.__fail_state_tag_name = 'failure'
        self.__skip_state_tag_name = 'skipped'
        self.__warn_state_tag_name = 'warning'

        self.__error_iter = iter(case.getElementsByTagName(self.__error_state_tag_name))
        self.__fail_iter = iter(case.getElementsByTagName(self.__fail_state_tag_name))
        self.__skip_iter = iter(case.getElementsByTagName(self.__skip_state_tag_name))
        self.__warn_iter = iter(case.getElementsByTagName(self.__warn_state_tag_name))

        self.__error = None
        self.__fail = None
        self.__skip = None
        self.__warn = None

    def next_error(self):
        next_value, self.__error = self.__next_iter_value(self.__error_iter)
        if not next_value:
            print(f"INFO: No more errors found")
        return next_value

    def error(self):
        return self.__error

    def next_fail(self):
        next_value, self.__fail = self.__next_iter_value(self.__fail_iter)
        if not next_value:
            print(f"INFO: No more fails found")
        return next_value

    def fail(self):
        return self.__fail

    def next_skip(self):
        next_value, self.__skip = self.__next_iter_value(self.__skip_iter)
        if not next_value:
            print(f"INFO: No more skips found")

        return next_value

    def skip(self):
        return self.__skip

    def next_warn(self):
        next_value, self.__warn = self.__next_iter_value(self.__warn_iter)
        if not next_value:
            print(f"INFO: No more warnings found")
        return next_value

    def warn(self):
        return self.__warn

    @staticmethod
    def __next_iter_value(iter_list):

        try:
            return True, iter_list.__next__()
        except StopIteration:
            return False, None