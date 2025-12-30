from lexer import Lexer

def test_compare():
    source = "a<=b >c=d#e<f"
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    types = [t.type for t in tokens]
    for t in tokens:
        print(t)

    assert types == [
        "IDENT", "LE", "IDENT", "GT", "IDENT", "EQ", "IDENT", "NEQ", "IDENT", "LT", "IDENT", "EOF"
    ]
