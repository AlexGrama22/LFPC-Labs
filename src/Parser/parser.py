class Parser:
    def __init__(self, token_generator):
        self.token_generator = token_generator
        self.tokens_list = []
        self.current_index = 0

    def consume(self):
        self.current_index += 1

    def current(self):
        return self.tokens_list[self.current_index]

    def process(self, input_expression):
        self.tokens_list = self.token_generator.tokenize(input_expression)
        self.current_index = 0
        return self.process_program()

    def process_program(self):
        code_structure = {
            'type': 'Program',
            'content': []
        }
        while self.current_index < len(self.tokens_list):
            statement = self.process_statement()
            code_structure['content'].append(statement)
        return code_structure

    def process_statement(self):
        token_category, _ = self.current()
        if token_category == 'VAR':
            return self.process_variable_declaration()
        # Add other statement types here...
        else:
            raise ValueError(f"Unexpected token: {token_category}")

    def process_variable_name(self):
        token_category, token_value = self.current()
        if token_category == 'ID':
            self.consume()
            return {
                'type': 'Identifier',
                'name': token_value
            }
        else:
            raise ValueError(f"Unexpected token: {token_category}")

    def process_value_expression(self):
        token_category, token_value = self.current()
        if token_category == 'INT':
            self.consume()
            return {
                'type': 'NumericLiteral',
                'value': int(token_value)
            }
        else:
            raise ValueError(f"Unexpected token: {token_category}")

    def process_variable_declaration(self):
        self.consume()  # Consume 'VAR'
        variable_name = self.process_variable_name()
        self.consume()  # Consume 'ASSIGN'
        value_expression = self.process_value_expression()
        self.consume()  # Consume 'SEMICOLON'

        return {
            'type': 'VariableDeclaration',
            'variable_name': variable_name,
            'value_expression': value_expression
        }

    def process(self):
        self.tokens_list = self.token_generator.tokenize()
        self.current_index = 0
        return self.process_program()

    def process_value_expression(self):
        token_category, token_value = self.current()
        if token_category == 'INT':
            self.consume()
            return {
                'type': 'NumericLiteral',
                'value': int(token_value)
            }
        elif token_category == 'ID':
            variable_name = token_value
            self.consume()
            if self.current()[0] == 'OP':
                operation = self.current()[1]
                self.consume()
                return {
                    'type': 'BinaryExpression',
                    'left': {
                        'type': 'Identifier',
                        'name': variable_name
                    },
                    'operator': operation,
                    'right': self.process_value_expression()
                }
            else:
                return {
                    'type': 'Identifier',
                    'name': variable_name
                }
        else:
            raise ValueError(f"Unexpected token: {token_category}")
