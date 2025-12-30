import pytest
from lexer import Lexer

def test_unknown():
    source = "x @ 5"
    lexer = Lexer(source)

    with pytest.raises(SyntaxError):
        lexer.tokenize()
