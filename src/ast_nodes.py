from dataclasses import dataclass
from typing import List


@dataclass
class Node:
    pass

@dataclass
class Statement(Node):
    pass

@dataclass
class Expr(Node):
    pass

@dataclass
class Condition(Node):
    pass


# -- Arithmetik ---

@dataclass
class Number(Expr):
    value: int

@dataclass
class Variable(Expr):
    name: str

@dataclass
class UnaryOp(Expr):
    op: str
    expr: Expr

@dataclass
class BinaryOp(Expr):
    op: str
    left: Expr
    right: Expr


# --- Bedingungen ---

@dataclass
class OddCondition(Condition):
    expr: Expr

@dataclass
class NormalCondition(Condition):
    left: Expr
    op: str
    right: Expr

# --- Statements ---
@dataclass
class Assign(Statement):
    name: str
    expr: Expr

@dataclass
class Call(Statement):
    name: str

@dataclass
class Read(Statement):
    name: str

@dataclass
class Write(Statement):
    expr: Expr

@dataclass
class If(Statement):
    condition: Condition
    then_stmt: Statement

@dataclass
class While(Statement):
    condition: Condition
    body: Statement

@dataclass
class BeginEnd(Statement):
    statements: List[Statement]


# --- Programm und Block---

@dataclass
class ConstDecl:
    name: str
    value: int

@dataclass
class VarDecl:
    name: str

@dataclass
class ProcDecl:
    name: str
    block: "Block"

@dataclass
class Block(Node):
    consts: List[ConstDecl]
    vars: List[VarDecl]
    procs: List[ProcDecl]
    statement: Statement

@dataclass
class Program(Node):
    block: Block
