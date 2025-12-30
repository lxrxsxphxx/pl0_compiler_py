from lexer import Lexer

def test_identifier():
    source = "x abc123 constx"
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    types = [t.type for t in tokens]
    for t in tokens:
        print(t)

    assert types == [
        "IDENT", "IDENT", "IDENT", "EOF"
    ]
