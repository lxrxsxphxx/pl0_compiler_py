from lexer import Lexer
from parser import Parser
from ast_nodes import *

def test_expression_precedence():
    source = "begin x := 1 + 2 * 3 end."

    program = Parser(Lexer(source).tokenize()).program()
    assign = program.block.statement.statements[0]
    expr = assign.expr

    assert expr.op == "PLUS"
    assert expr.right.op == "TIMES"
