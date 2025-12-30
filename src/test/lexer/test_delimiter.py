from lexer import Lexer

def test_delimiters():
    source = "( ) , ; . "
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    types = [t.type for t in tokens]
    for t in tokens:
        print(t)

    assert types == [
        "LPAREN","RPAREN", "COMMA", "SEMICOLON", "DOT", "EOF"
    ]
