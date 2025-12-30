from lexer import Lexer

def test_arithmetic():
    source = "a+b-c*d/e"
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    types = [t.type for t in tokens]
    for t in tokens:
        print(t)

    assert types == [
        "IDENT", "PLUS", "IDENT", "MINUS", "IDENT", "TIMES", "IDENT", "SLASH", "IDENT", "EOF"
    ]
    