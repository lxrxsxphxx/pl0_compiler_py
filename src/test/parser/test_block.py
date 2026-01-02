from lexer import Lexer
from parser import Parser
from ast_nodes import *

def test_block():
    source = "var x; begin x := 1 end."

    program = Parser(Lexer(source).tokenize()).program()
    block = program.block

    assert len(block.vars) == 1
    assert block.vars[0].name == "x"
    assert block.consts == []
    assert block.procs == []
