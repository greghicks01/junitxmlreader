import pytest


@pytest.mark.skip('skip untagged')
def test_skip_untagged():
    pass


@pytest.mark.skip('skip tagged')
def test_skip_tagged(record_property):
    record_property('Test Case', 'skiptag')
    pass


@pytest.mark.skipif(1 < 2, reason='skip if 1 < 2')
def test_skipif_true_untag():
    pass


@pytest.mark.skipif(2 < 1, reason='skipif 2 < 1')
def test_skipif_false_untag():
    pass


@pytest.mark.skipif(1 < 2, reason='skip if 1 < 2')
def test_skipif_true_tag(record_property):
    record_property('Test Case', 'skipif_true_tag')
    pass


@pytest.mark.skipif(2 < 1, reason='skipif 2 < 1')
def test_skipif_false_tag(record_property):
    record_property('Test Case', 'skipif_false_tag')
    pass


@pytest.mark.xfail()
def test_xfail_untag():
    pytest.fail()


@pytest.mark.xfail()
def test_xfail_tag(record_property):
    record_property('Test Case', 'fail tag')
    pytest.fail()


def test_failed_untag():
    pytest.fail()


def test_failed_tag(record_property):
    record_property('Test Case', 'testfailed')
    pytest.fail()

def test_bad_state(record_property):
    record_property('Test Case', 'bad state')
    print('test error')
    f