from lexer import Lexer

def test_minimal_input():
    source = ""

    lexer = Lexer(source)
    tokens = lexer.tokenize()

    for t in tokens:
        print(t)

    types = [t.type for t in tokens]

    assert types == [
        "EOF"
    ]
