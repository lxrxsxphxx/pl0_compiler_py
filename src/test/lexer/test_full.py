from lexer import Lexer

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


    lexer = Lexer(source)
    tokens = lexer.tokenize()

    types = [t.type for t in tokens]
    for t in tokens:
        print(t)

    assert types == [
        # var a,fak;
        "VAR", "IDENT", "COMMA", "IDENT", "SEMICOLON",

        # procedure p1;
        "PROCEDURE", "IDENT", "SEMICOLON",

        # var b,c;
        "VAR", "IDENT", "COMMA", "IDENT", "SEMICOLON",

        "BEGIN",

        # b := a;
        "IDENT", "ASSIGN", "IDENT", "SEMICOLON",

        # a := a-1;
        "IDENT", "ASSIGN", "IDENT", "MINUS", "NUMBER", "SEMICOLON",

        # c := a;
        "IDENT", "ASSIGN", "IDENT", "SEMICOLON",

        # !c;
        "WRITE", "IDENT", "SEMICOLON",

        # if c>1 then call p1;
        "IF", "IDENT", "GT", "NUMBER", "THEN", "CALL", "IDENT", "SEMICOLON",

        # fak := fak*b;
        "IDENT", "ASSIGN", "IDENT", "TIMES", "IDENT", "SEMICOLON",

        # !fak
        "WRITE", "IDENT",

        # end;
        "END", "SEMICOLON",

        # begin
        "BEGIN",

        # ?a;
        "READ", "IDENT", "SEMICOLON",

        # fak := 1;
        "IDENT", "ASSIGN", "NUMBER", "SEMICOLON",

        # call p1;
        "CALL", "IDENT", "SEMICOLON",

        # !fak
        "WRITE", "IDENT",

        "END", "DOT",
        "EOF"
    ]

