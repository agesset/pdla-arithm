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