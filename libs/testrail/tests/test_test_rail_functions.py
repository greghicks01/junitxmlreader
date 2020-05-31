from libs.testrail.testrail.testrail_functions import TestRailFunctions


url = 'https://greg595.testrail.io/'
name = ''
key = ''
project_id = 1
suite_id = 2
test_case_ids = {2: 1, 8: 5, 9: 1}


def test_test_rail_setup():
    url = ''
    name = ''
    key = ''
    test_rail_functions = TestRailFunctions(url, name, key, project_id, suite_id)
    assert test_rail_functions is not None


def test_rail_add_run():
    test_rail_functions = TestRailFunctions(url, name, key, project_id, suite_id)
    test_rail_functions.project_id = project_id
    test_rail_functions.add_new_run()

    assert test_rail_functions.run_id != ''


def test_rail_add_case_result():
    test_rail_functions = TestRailFunctions(url, name, key, project_id, suite_id)
    test_rail_functions.project_id = project_id
    test_rail_functions.add_new_run()
    test_rail_functions.add_case_result(2, 1, elapsed_time='2')

    assert test_rail_functions.result_id != -1


def test_rail_add_attachment():
    test_rail_functions = TestRailFunctions(url, name, key, project_id, suite_id)
    test_rail_functions.project_id = project_id
    test_rail_functions.add_new_run()
    test_rail_functions.add_case_result(2, 1, elapsed_time='2')
    test_rail_functions.add_attachment_to_result('C:\\globdata.ini')


def test_rail_iterate_cases():
    test_rail_functions = TestRailFunctions(url, name, key, project_id, suite_id)
    test_rail_functions.add_new_run()

    for case_key in test_case_ids:
        test_rail_functions.add_case_result(case_key, test_case_ids[case_key], elapsed_time='2')
