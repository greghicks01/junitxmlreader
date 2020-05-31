import os

from libs.testrail.testrail.testrail import APIClient, APIError


class TestRailFunctions:

    def __init__(self, url, username, password):

        # Gurock's supplied code
        self.testrail = APIClient(url)
        self.testrail.user = username
        self.testrail.password = password

        # set this externally
        self.project_id: int = -1

        # internal values - do not set externally
        self.run_id: int = -1
        self.result_id: int = -1
        self.suite_id: int = -1
        self.case_id: int = -1

        # TestRail API path tails - rest of path is in testrail
        self.add_run = 'add_run/{self.project_id}'
        self.add_result_for_case = 'add_result_for_case/{self.run_id}/{self.case_id}'
        self.attachments = 'add_attachment_to_result/{self.result_id}'
        self.close_run = 'close_run/{self.run_id}'

    def add_new_run(self, suite_id: int):
        data = {"suite_id": suite_id}
        packet = self.testrail.send_post(eval("f'" + self.add_run + "'"), data)

        self.run_id = packet['id']

    def add_case_result(self, case_id, status: int, comment=None, elapsed_time=None):

        # Status values 1 or 5 only (Pass,Fail)
        if status != 1 and status != 5:
            raise Exception(f'Status value expected to be 1 or 5, received "{status}"')

        self.case_id = case_id

        payload = {'status_id': status, 'comment': comment, 'elapsed': elapsed_time + "s"}

        result = self.testrail.send_post(
            eval("f'" + self.add_result_for_case + "'"),
            payload
        )

        self.result_id = result['id']

    def add_attachment_to_result(self, file_path):

        if not os.path.isfile(file_path):
            raise FileNotFoundError(f'File {file_path} does not exist')

        result = self.testrail.send_post(
            eval("f'" + self.attachments + "'"),
            file_path
        )

    def __del__(self):
        data = {}
        result = self.testrail.send_post(
            eval("f'" + self.close_run + "'"),
            data
        )

