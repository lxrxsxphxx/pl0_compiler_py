from lexer import tokenize

source = """
const x = 10;
var y;
begin
    y := x + 1;
end.
"""

for token in tokenize(source):
    print(token)
