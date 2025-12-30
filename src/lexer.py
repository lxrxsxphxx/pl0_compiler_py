'''
Lexer module for tokenizing source code.

scope:
Run through the input character by character
Recognise tokens

lexer.py
├── Token (Datentyp)
├── TokenType (Konstanten / Enum)
├── KEYWORDS
├── Lexer (Klasse)
│   ├── __init__()
│   ├── tokenize()
│   ├── _advance()
│   ├── _peek()
│   ├── _skip_whitespace()
│   ├── _read_identifier()
│   ├── _read_number()
└── LexerError

'''


from dataclasses import dataclass

# --- Token Datentyp ---

@dataclass
class Token:
    type: str
    value: str
    line: int
    column: int


# --- Token Types ---

IDENT = "IDENT"
NUMBER = "NUMBER"
EOF = "EOF"

READ  = "READ"
WRITE = "WRITE"

# Operators
ASSIGN = "ASSIGN"
PLUS = "PLUS"
MINUS = "MINUS"
TIMES = "TIMES"
SLASH = "SLASH"

EQ  = "EQ"    # =
NEQ = "NEQ"   # ! (in PL0 aber #)
LT  = "LT"    # <
LE  = "LE"    # <=
GT  = "GT"    # >
GE  = "GE"    # >=


# Delimiters
LPAREN = "LPAREN"
RPAREN = "RPAREN"
COMMA = "COMMA"
SEMICOLON = "SEMICOLON"
DOT = "DOT"


# --- Keywords ---

KEYWORDS = {
    "const": "CONST",
    "var": "VAR",
    "procedure": "PROCEDURE",
    "call": "CALL",
    "begin": "BEGIN",
    "end": "END",
    "if": "IF",
    "then": "THEN",
    "while": "WHILE",
    "do": "DO",
    "read": "READ",
    "write": "WRITE",
}

# --- Lexer ---

class Lexer:
    def __init__(self, source: str):
        self.source = source
        self.pos = 0
        self.line = 1
        self.column = 1
        self.tokens = []

    # Tokenize the input source code
    def tokenize(self):
        while self.pos < len(self.source):
            ch = self._peek()

            if ch.isspace():
                self._skip_whitespace()
            elif ch.isalpha():
                self._read_identifier()
            elif ch.isdigit():
                self._read_number()
            else:
                self._read_symbol()

        self.tokens.append(Token(EOF, "", self.line, self.column))
        return self.tokens

    # --- Helper Methods ---
    def _peek(self):
        if self.pos < len(self.source):
            return self.source[self.pos]
        return None

    def _advance(self):
        ch = self.source[self.pos]
        self.pos += 1
        self.column += 1
        return ch

    def _skip_whitespace(self):
        while self.pos < len(self.source) and self._peek().isspace():
            if self._peek() == "\n":
                self.line += 1
                self.column = 1
            else:
                self.column += 1
            self.pos += 1

    def _read_identifier(self):
        start_col = self.column
        start = self.pos

        while self.pos < len(self.source) and self._peek().isalnum():
            self._advance()

        value = self.source[start:self.pos]
        value = value.lower()
        token_type = KEYWORDS.get(value, IDENT)

        self.tokens.append(Token(token_type, value, self.line, start_col))

    def _read_number(self):
        start_col = self.column
        start = self.pos

        while self.pos < len(self.source) and self._peek().isdigit():
            self._advance()

        value = self.source[start:self.pos]
        self.tokens.append(Token(NUMBER, value, self.line, start_col))

    def _read_symbol(self):
        start_col = self.column
        ch = self._advance()

        # Zuweisung
        if ch == ":" and self._peek() == "=":
            self._advance()
            self.tokens.append(Token(ASSIGN, ":=", self.line, start_col))

        # Vergleichsoperatoren
        elif ch == "=":
            self.tokens.append(Token(EQ, ch, self.line, start_col))

        elif ch == "#":
            self.tokens.append(Token(NEQ, ch, self.line, start_col))

        elif ch == "<":
            if self._peek() == "=":
                self._advance()
                self.tokens.append(Token(LE, "<=", self.line, start_col))
            else:
                self.tokens.append(Token(LT, "<", self.line, start_col))

        elif ch == ">":
            if self._peek() == "=":
                self._advance()
                self.tokens.append(Token(GE, ">=", self.line, start_col))
            else:
                self.tokens.append(Token(GT, ">", self.line, start_col))

        # Arithmetik
        elif ch == "+":
            self.tokens.append(Token(PLUS, ch, self.line, start_col))
        elif ch == "-":
            self.tokens.append(Token(MINUS, ch, self.line, start_col))
        elif ch == "*":
            self.tokens.append(Token(TIMES, ch, self.line, start_col))
        elif ch == "/":
            self.tokens.append(Token(SLASH, ch, self.line, start_col))

        # Trennzeichen
        elif ch == ";":
            self.tokens.append(Token(SEMICOLON, ch, self.line, start_col))
        elif ch == "(":
            self.tokens.append(Token(LPAREN, ch, self.line, start_col))
        elif ch == ")":
            self.tokens.append(Token(RPAREN, ch, self.line, start_col))
        elif ch == ",":
            self.tokens.append(Token(COMMA, ch, self.line, start_col))
        elif ch == ".":
            self.tokens.append(Token(DOT, ch, self.line, start_col))

        # Eingabe / Ausgabe
        elif ch == "!":
            self.tokens.append(Token(WRITE, ch, self.line, start_col))
        elif ch == "?":
            self.tokens.append(Token(READ, ch, self.line, start_col))

        else:
            raise SyntaxError(
                f"Unbekanntes Zeichen '{ch}' "
                f"in Zeile {self.line}, Spalte {start_col}"
            )

