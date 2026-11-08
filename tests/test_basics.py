import pytest

from arithmp.parser import Parser


def test_add():
    parse = Parser()
    assert parse.parse("3 + 4") == 7.0

def test_mul():
    parse = Parser()
    assert parse.parse("3 * 4") == 12.0

def test_sub():
    parse = Parser()
    assert parse.parse("7 - 4") == 3.0

def test_mod():
    parse = Parser()
    assert parse.parse("4 % 3") == 1.0

def test_div():
    parse = Parser()
    assert parse.parse("8 / 2") == 4.0

def test_assignment():
    p = Parser()
    assert p.parse("a = 4") is None
    assert p.parse("a + 1") == 5


def test_constants():
    assert Parser().parse("pi") == pytest.approx(3.14159, abs=1e-4)


def test_unknown_variable():
    with pytest.raises(ValueError):
        Parser().parse("b + 1")