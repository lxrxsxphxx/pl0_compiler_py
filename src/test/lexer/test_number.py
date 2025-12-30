from lexer import Lexer

def test_numbers():
    source = "0 1 42 999 123abc"
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    types = [t.type for t in tokens]
    for t in tokens:
        print(t)

    assert types == [
        "NUMBER", "NUMBER", "NUMBER", "NUMBER", "NUMBER", "IDENT", "EOF"
    ]
