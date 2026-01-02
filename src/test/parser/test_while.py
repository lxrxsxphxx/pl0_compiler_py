from lexer import Lexer
from parser import Parser
from ast_nodes import *

def test_while_statement():
    source = "begin while x > 0 do x := x - 1 end."

    program = Parser(Lexer(source).tokenize()).program()
    stmt = program.block.statement.statements[0]

    assert stmt.__class__.__name__ == "While"
