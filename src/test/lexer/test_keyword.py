from lexer import Lexer

def test_keywords():
    source = "const var procedure call begin end if then while do read write"
    lexer = Lexer(source)
    tokens = lexer.tokenize()

    types = [t.type for t in tokens]
    for t in tokens:
        print(t)

    assert types == [
        "CONST", "VAR", "PROCEDURE", "CALL", "BEGIN", "END", "IF", "THEN", "WHILE", "DO", "READ", "WRITE", "EOF"
    ]
