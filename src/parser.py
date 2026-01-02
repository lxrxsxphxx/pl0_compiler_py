from lexer import Lexer
from ast_nodes import *

class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def current(self):
        return self.tokens[self.pos]

    def consume(self, expected_type):
        token = self.current()
        if token.type == expected_type:
            self.pos += 1
            return token
        else:
            raise SyntaxError(
                f"Erwartet {expected_type}, "
                f"bekommen {token.type} "
                f"(Zeile {token.line}, Spalte {token.column})"
            )


    def program(self):
        # program    = block "." .

        block = self.block()
        self.consume("DOT")
        self.consume("EOF") # ende prüfen sonst loop
        return Program(block)

    

    def block(self):
        # block      = [ "CONST" ident "=" number { "," ident "=" number } ";" ]
        #              [ "VAR" ident { "," ident } ";" ]
        #              { "PROCEDURE" ident ";" block ";" }
        #              statement .

        consts = []
        vars = []
        procs = []

        # "CONST" ident "=" number { "," ident "=" number } ";"
        if self.current().type == "CONST":
            self.consume("CONST")
            while True:
                name = self.consume("IDENT").value
                self.consume("EQ")
                value = int(self.consume("NUMBER").value)
                consts.append(ConstDecl(name, value))
                if self.current().type != "COMMA":
                    break
                self.consume("COMMA")
            self.consume("SEMICOLON")

        # "VAR" ident { "," ident } ";"
        if self.current().type == "VAR":
            self.consume("VAR")
            while True:
                name = self.consume("IDENT").value
                vars.append(VarDecl(name))
                if self.current().type != "COMMA":
                    break
                self.consume("COMMA")
            self.consume("SEMICOLON")

        # "PROCEDURE" ident ";" block ";"
        while self.current().type == "PROCEDURE":
            self.consume("PROCEDURE")
            name = self.consume("IDENT").value
            self.consume("SEMICOLON")
            proc_block = self.block()
            self.consume("SEMICOLON")
            procs.append(ProcDecl(name, proc_block))

        # Statement
        stmt = self.statement()

        return Block(consts, vars, procs, stmt)


# --- Statements und stuff also ? und !  und begin while und stuff---

    def statement(self):
        # statement  = [ ident ":=" expression | "CALL" ident | "?" ident | "!" expression |
        #                "BEGIN" statement { ";" statement } "END" |
        #                "IF" condition "THEN" statement |
        #                "WHILE" condition "DO" statement ] .
        
        token = self.current()

        # ident ":=" expression
        if token.type == "IDENT":
            name = self.consume("IDENT").value
            self.consume("ASSIGN")
            expr = self.expression()
            return Assign(name, expr)

        # "CALL" ident 
        elif token.type == "CALL":
            self.consume("CALL")
            name = self.consume("IDENT").value
            return Call(name)

        # "?" ident
        elif token.type == "READ":
            self.consume("READ")
            name = self.consume("IDENT").value
            return Read(name)

        # "!" expression
        elif token.type == "WRITE":
            self.consume("WRITE")
            expr = self.expression()
            return Write(expr)
        

        # "BEGIN" statement { ";" statement } "END"
        elif token.type == "BEGIN":
            self.consume("BEGIN")

            statements = []

            # erstes Statement (Pflicht!)
            statements.append(self.statement())

            # weitere Statements nach ;
            while self.current().type == "SEMICOLON":
                self.consume("SEMICOLON")
                statements.append(self.statement())

            self.consume("END")

            return BeginEnd(statements)

        # "IF" condition "THEN" statement
        elif token.type == "IF":
            self.consume("IF")
            condition = self.condition()

            self.consume("THEN")
            then_stmt = self.statement()

            return If(condition, then_stmt)

        # "WHILE" condition "DO" statement
        elif token.type == "WHILE":
            self.consume("WHILE")
            condition = self.condition()

            self.consume("DO")
            body = self.statement()

            return While(condition, body)


        # leeres Statement
        else:
            return None
        

    def condition(self):
        # condition  = "ODD" expression | expression ("=" | "#" | "<" | "<=" | ">" | ">=") expression .
        token = self.current()

        # ODD condition
        if token.type == "ODD":
            self.consume("ODD")
            expr = self.expression()
            return OddCondition(expr)

        # normal condition
        left = self.expression()

        op_token = self.current()
        if op_token.type not in {"EQ", "NEQ", "LT", "LE", "GT", "GE"}:
            raise SyntaxError(
                f"Vergleichsoperator erwartet, "
                f"bekommen {op_token.type} "
                f"(Zeile {op_token.line}, Spalte {op_token.column})"
            )

        self.consume(op_token.type)
        right = self.expression()

        return NormalCondition(left, op_token.type, right)
    
# --- Arithmetik ---
    def expression(self):
        # expression = [ "+" | "-" ] term { ( "+" | "-" ) term } .

        if self.current().type in ("PLUS", "MINUS"):
            op = self.current().type
            self.consume(op)
            node = UnaryOp(op, self.parse_term())
        else:
            node = self.parse_term()

        while self.current().type in ("PLUS", "MINUS"):
            op = self.current().type
            self.consume(op)
            right = self.parse_term()
            node = BinaryOp(op, node, right)

        return node


    def term(self):
        #term       = factor { ( "*" | "/" ) factor } .
        node = self.parse_factor()

        while self.current().type in ("TIMES", "SLASH"):
            op = self.current().type
            self.consume(op)
            right = self.parse_factor()
            node = BinaryOp(op, node, right)

        return node


    def factor(self):
        # factor     = ident | number | "(" expression ")" .

        tok = self.current()

        if tok.type == "IDENT":
            self.consume("IDENT")
            return Variable(tok.value)

        elif tok.type == "NUMBER":
            self.consume("NUMBER")
            return Number(int(tok.value))

        elif tok.type == "LPAREN":
            self.consume("LPAREN")
            expr = self.parse_expression()
            self.consume("RPAREN")
            return expr

        else:
            raise SyntaxError(
                f"Unerwartetes Token {tok.type} "
                f"(Zeile {tok.line}, Spalte {tok.column})"
            )





