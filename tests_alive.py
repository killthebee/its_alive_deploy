from app import is_alive_host


def test_live():
    assert is_alive_host('semrush.com') == {'status': 'up'}


def test_down_a():
    assert is_alive_host('invalid.domain.son') == {'status': 'down'}


def test_down_b():
    assert is_alive_host('semrush55555555555555555555.com') == {'status': 'down'}
