from utils import plural, TimeUnit


def test_plural():
    assert plural('apple') == 'apples'
    assert plural('dish') == 'dishes'
    assert plural('dish', count=1) == 'dish'


def test_time_unit():
    assert TimeUnit.duration(0) == ''
    assert TimeUnit.duration(1) == '1 second'
    assert TimeUnit.duration(2) == '2 seconds'
    assert TimeUnit.duration(60) == '1 minute'
    assert TimeUnit.duration(121) == '2 minutes'
    assert TimeUnit.duration(3600) == '1 hour'
    assert TimeUnit.duration(3600 * 2) == '2 hours'
    assert TimeUnit.duration(86400) == '1 day'
    assert TimeUnit.duration(86400 * 2) == '2 days'
    assert TimeUnit.duration(86400 * 7) == '1 week'
    assert TimeUnit.duration(86400 * 14) == '2 weeks'
    assert TimeUnit.duration(86400 * 30) == '1 month'
    assert TimeUnit.duration(86400 * 30 * 2) == '2 months'
    assert TimeUnit.duration(86400 * 365) == '1 year'
    assert TimeUnit.duration(86400 * 365 * 2) == '2 years'
    assert TimeUnit.duration(86400 * 365 * 2 + 86400 * 30 + 86400 * 2 + 3600 + 60 * 2 + 1, first=False) == \
        '2 years 1 month 2 days 1 hour 2 minutes 1 second'
