import re

class MathLexer:
    TOKENS = [
        (r'\s+', None),  # Ignore whitespace
        (r'\d*\.\d+([eE][-+]?\d+)?', 'FLOAT'),  # Floating point numbers
        (r'\d+', 'INT'),  # Integers
        (r'[+\-*/]', 'OP'),  # Arithmetic operators
        (r'\(', 'LPAREN'),  # Left parenthesis
        (r'\)', 'RPAREN'),  # Right parenthesis
        (r'var', 'VAR'),  # var keyword
        (r'[a-zA-Z_][a-zA-Z0-9_]*', 'ID'),  # Identifiers
        (r'=', 'ASSIGN'),  # Assignment operator
        (r';', 'SEMICOLON')  # Statement termination symbol
    ]

    def __init__(self, expression):
        self.expression = expression
        self.tokens = []

    def tokenize(self):
        while len(self.expression) > 0:
            matched = False
            for pattern, token_type in self.TOKENS:
                regex = re.compile(pattern)
                match = regex.match(self.expression)
                if match:
                    matched = True
                    if token_type:  # Only non-None token types will be appended
                        token = (token_type, match.group(0))
                        self.tokens.append(token)
                    self.expression = self.expression[len(match.group(0)):]
                    break
            if not matched:
                raise ValueError(f"Invalid token: {self.expression}")
        return self.tokens

