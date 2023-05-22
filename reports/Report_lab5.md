# Parser & Building an Abstract Syntax Tree

## Course: Formal Languages & Finite Automata  
## Author: Grama Alexandru




## Theory

The process of gathering syntactical meaning or doing a syntactical analysis over some text can also be called parsing. It usually results in a parse tree which can also contain semantic information that could be used in subsequent stages of compilation, for example.

    Similarly to a parse tree, in order to represent the structure of an input text one could create an Abstract Syntax Tree (AST). This is a data structure that is organized hierarchically in abstraction layers that represent the constructs or entities that form up the initial text. These can come in handy also in the analysis of programs or some processes involved in compilation.
## Objectives

1. Get familiar with parsing, what it is and how it can be programmed [^1].
2. Get familiar with the concept of AST [^2].
3. In addition to what has been done in the 3rd lab work, do the following:
    1. In case you didn't have a type that denotes the possible types of tokens, you need to:
        1. Have a type TokenType (like an enum) that can be used in the lexical analysis to categorize the tokens.
        2. Please use regular expressions to identify the type of the token.
    2. Implement the necessary data structures for an AST that could be used for the text you have processed in the 3rd lab work.
    3. Implement a simple parser program that could extract the syntactic information from the input text.


## Implementation description

### Parser Class

This constructor method sets up the initial state of the class by assigning the token generator, initializing the list for tokens, and setting the current index to 0.
```python
    def __init__(self, token_generator):
        self.token_generator = token_generator
        self.tokens_list = []
        self.current_index = 0
```

### Parsing
The `process_statement` method checks the category of the current token. If it is a variable declaration ('VAR'), it processes the variable declaration statement. Otherwise, it raises a ValueError with an appropriate error message for unexpected tokens.
```python
   def process_statement(self):
        token_category, _ = self.current()
        if token_category == 'VAR':
            return self.process_variable_declaration()
        # Add other statement types here...
        else:
            raise ValueError(f"Unexpected token: {token_category}")
    
```
### Processing the variable names and values

Both methods follow a similar pattern. They retrieve the current token, perform a check based on the token's category, consume the token if it matches the expected category, and return the processed result. If the token's category does not match the expected value, they raise a `ValueError` with an appropriate error message indicating the unexpected token.

These methods are likely used by the parser to process specific parts of the input expression and build an abstract syntax tree (AST) representing the parsed structure.
```python
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

```

### Processing a token sequence

The method essentially builds and returns an AST node representing a variable declaration statement with the variable name and its assigned value expression.
```python
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

```

### Processing a token sequence that represents a value expression
The method essentially processes the token sequence representing a value expression and constructs an appropriate AST node for the value expression based on its type (numeric literal, identifier, or binary expression).
```python
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
```


### Interpreter 
The Interpreter class provides a way to interpret and evaluate the AST generated from the parsed code. It supports variable declaration, numeric literals, identifier references, and basic binary expressions.
```python
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



```
# Input:
```
var m = 21; 
var x = 3; 
var z = m + x;
```
# Results:
```
{'type': 'Program', 'content': [{'type': 'VariableDeclaration', 'variable_name': {'type': 'Identifier', 'name': 'm'}, 'value_expression': {'type': 'NumericLiteral', 'value': 21}}, {'type': 'VariableDeclaration', 'variable_name': {'type': 'Identifier', 'name': 'x'}, 'value_expression': {'type': 'NumericLiteral', 'value': 3}}, {'type': 'VariableDeclaration', 'variable_name': {'type': 'Identifier', 'name': 'z'}, 'value_expression': {'type': 'BinaryExpression', 'left': {'type': 'Identifier', 'name': 'm'}, 'operator': '+', 'right': {'type': 'Identifier', 'name': 'x'}}}]}
{'m': 21, 'x': 3, 'z': 24}
```

# Conclusion

Parsers and interpreters are fundamental components in the field of programming languages and software development. They are essential for analyzing and executing code, enabling the transformation of human-readable code into machine-executable instructions. Understanding the concepts and principles behind parsers and interpreters is crucial for building programming languages, compilers, interpreters, and other tools related to code analysis and execution.

Parsers are responsible for breaking down source code into its constituent parts, such as tokens or abstract syntax trees (ASTs), based on the rules of a formal grammar. They play a critical role in validating the syntax of code and providing a structured representation that can be further processed or executed.

ASTs serve as an intermediate representation of source code, capturing its syntactic structure in a hierarchical tree format. ASTs provide a higher-level abstraction that simplifies code manipulation, analysis, and transformation. They facilitate tasks such as code optimization, static analysis, refactoring, and more.

Interpreters, on the other hand, take the parsed code, typically represented as an AST, and execute it directly. Interpreters evaluate the code in a step-by-step manner, producing results or performing actions as directed by the code. They are commonly used in scripting languages and interactive environments, offering dynamic execution and immediate feedback.

Understanding the intricacies of parsers and interpreters empowers software developers to work with programming languages more effectively. It enables them to create new languages, design compilers, implement interpreters, and build advanced code analysis tools. Furthermore, parsers and interpreters play a vital role in enhancing productivity, enabling software engineers to write efficient code, identify and fix errors, and create robust applications.

As technology continues to evolve, parsers and interpreters will remain essential tools for processing and executing code. Whether it's developing new programming languages, optimizing performance, or creating innovative software tools, a strong grasp of parsers and interpreters is invaluable in the ever-expanding world of software development.