from lexer import Lexer

def test_allocation():
    source = "x := 10;"

    lexer = Lexer(source)
    tokens = lexer.tokenize()
    for t in tokens:
        print(t)

    types = [t.type for t in tokens]

    assert types == [
        "IDENT", "ASSIGN", "NUMBER", "SEMICOLON", "EOF"
    ]
