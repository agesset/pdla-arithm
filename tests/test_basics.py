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


def test_calls():
    parse = Parser().parse
    assert parse("abs(-4)") == 4
    assert parse("round(2.6)") == 3
    assert parse("max(1, 5, 3)") == 5
    assert parse("abs(-4) + 1") == 5


def test_unknown_function():
    with pytest.raises(ValueError):
        Parser().parse("foo(1)")
