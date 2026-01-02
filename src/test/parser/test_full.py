from lexer import Lexer
from parser import Parser
from ast_nodes import *

def test_full():
    source = """
        var a,fak;
        procedure p1;
        var b,c;
        begin
        b := a;
        a := a-1;
        c := a;
        !c;
        if c>1 then call p1;
        fak := fak*b;
        !fak
        end;
        begin
        ?a;
        fak := 1;
        call p1;
        !fak
        end.
    """

    tokens = Lexer(source).tokenize()
    parser = Parser(tokens)

    program = parser.program()

    assert isinstance(program, Program)
