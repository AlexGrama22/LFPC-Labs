class Interpreter:
    def __init__(self):
        self.variables = {}

    def interpret(self, ast):
        if ast['type'] == 'Program':
            for statement in ast['content']:
                self.interpret(statement)
        elif ast['type'] == 'VariableDeclaration':
            variable_name = ast['variable_name']['name']
            value_expression = ast['value_expression']
            self.variables[variable_name] = self.interpret(value_expression)
        elif ast['type'] == 'NumericLiteral':
            return ast['value']
        elif ast['type'] == 'Identifier':
            variable_name = ast['name']
            if variable_name in self.variables:
                return self.variables[variable_name]
            else:
                raise ValueError(f"Undefined variable: {variable_name}")
        elif ast['type'] == 'BinaryExpression':
            left_value = self.interpret(ast['left'])
            right_value = self.interpret(ast['right'])
            operator = ast['operator']
            if operator == '+':
                return left_value + right_value
            # Add other operators here...
        else:
            raise ValueError(f"Unknown node type: {ast['type']}")
