from pytest import raises
from syt.templating import escaping_split


def test_escaping_split():
    assert escaping_split('a,b') == ['a', 'b']
    assert escaping_split('[a, b, c],[d, e, f]') == ['[a, b, c]', '[d, e, f]']
    assert escaping_split('"a, b, c","d, e, f"') == ['"a, b, c"', '"d, e, f"']

    with raises(AssertionError):
        assert escaping_split('[a, b, c,[d, e, f]') == ['[a, b, c]', '[d, e, f]']
