from lexer import Lexer
from parser import Parser
from ast_nodes import *

def test_if_statement():
    source = "begin if x > 0 then x := 1 end."

    program = Parser(Lexer(source).tokenize()).program()
    stmt = program.block.statement.statements[0]

    assert stmt.__class__.__name__ == "If"
