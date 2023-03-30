import re

class MathLexer:
    TOKENS = [
        (r'\s+', None),  # Ignore whitespace
        (r'\d*\.\d+([eE][-+]?\d+)?', 'FLOAT'),  # Floating point numbers
        (r'\d+', 'INT'),  # Integers
        (r'[+\-*/]', 'OP'),  # Arithmetic operators
        (r'\(', 'LPAREN'),  # Left parenthesis
        (r'\)', 'RPAREN'),  # Right parenthesis
    ]

    def __init__(self, expression):
        self.tokens = self._tokenize(expression)

    def _tokenize(self, expression):
        tokens = []
        while expression:
            for pattern, token_type in self.TOKENS:
                match = re.match(pattern, expression)
                if match:
                    value = match.group(0)
                    if token_type:
                        tokens.append((token_type, value))
                    expression = expression[len(value):]
                    break
            else:
                raise SyntaxError(f"Invalid syntax: {expression}")
        return tokens
