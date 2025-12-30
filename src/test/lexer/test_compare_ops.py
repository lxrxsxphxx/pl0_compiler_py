from lexer import Lexer

def test_compare_ops():
    source = "= # < <= > >="
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    types = [t.type for t in tokens]
    for t in tokens:
        print(t)

    assert types == [
        "EQ", "NEQ", "LT", "LE", "GT", "GE", "EOF"
    ]
