# Lexer & Scanner
## Course: Formal Languages & Finite Automata
## Author: Grama Alexandru FAF-211





## Theory
    The term lexer comes from lexical analysis which, in turn, represents the process of extracting lexical tokens from a string of characters. There are several alternative names for the mechanism called lexer, for example tokenizer or scanner. The lexical analysis is one of the first stages used in a compiler/interpreter when dealing with programming, markup or other types of languages. The tokens are identified based on some rules of the language and the products that the lexer gives are called lexemes. So basically the lexer is a stream of lexemes. Now in case it is not clear what's the difference between lexemes and tokens, there is a big one. The lexeme is just the byproduct of splitting based on delimiters, for example spaces, but the tokens give names or categories to each lexeme. So the tokens don't retain necessarily the actual value of the lexeme, but rather the type of it and maybe some metadata.

## Objectives:
- Understand what lexical analysis [1] is.

- Get familiar with the inner workings of a lexer/scanner/tokenizer.

- Implement a sample lexer and show how it works.
  

## Implementation description
### Lexer class
The Lexer class in Python is responsible for parsing an input string and identifying the various types of tokens present in the string. To do this, the class defines a set of regular expression patterns that match different token types such as operators, identifiers, keywords, numbers, strings, and more. When the class's tokenize method is called, it iterates over these patterns, attempting to match them against the input string. If a match is found, the corresponding token and its value are added to a list of tokens. In case an invalid token is encountered, the class raises a ValueError exception.
```python
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


```
### Tokenize method
The Lexer class's tokenize method accepts a string input and returns a token list. It accomplishes this by looping through the list of token patterns in the Lexer instance's self.token_patterns attribute. The method utilizes regular expressions to match each pattern to the start of the input string. If a match is detected, the method combines the token type and matched string to create a token, which it then adds to the token list stored in the Lexer instance's self.tokens attribute.

If a match is found, the method modifies the input string by removing the matched section. This process is repeated until the entire input string has been processed. If a pattern is not matched to any portion of the input string, the method will throw a ValueError containing an error message indicating an invalid token was encountered.

Lastly, the method returns the token list that was generated.
```python
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
```
### Main
The Main class imports the Lexer class from the lexer module, and then creates an instance of the Lexer class by invoking its constructor without any arguments. Subsequently, the tokenize method of the Lexer instance is invoked with the input string "2 * (21/2) + (3 + 4) - 5 / 6". The method tokenizes the input string by separating it into a list of tokens and then returns the list. Finally, the resulting list of tokens is printed to the console using the print function. The output confirms that the input string has been correctly tokenized into its component tokens, including numbers, operators, and parentheses. Moreover, the message "input valid" is printed to the console, indicating that the input string was tokenized successfully without encountering any errors.```python
```python
from lexer import Lexer
class Main:
    lexer = Lexer()
    lexer = MathLexer('2 * (21/2) + (3 + 4) - 5 / 6')
    tokens = lexer.tokens
    print(tokens)

```



## Results
[('INT', '2'), ('OP', '*'), ('LPAREN', '('), ('INT', '21'), ('OP', '/'), ('INT', '2'), ('RPAREN', ')'), ('OP', '+'), ('LPAREN', '('), ('INT', '3'), ('OP', '+'), ('INT', '4'), ('RPAREN', ')'), ('OP', '-'), ('INT', '5'), ('OP', '/'), ('INT', '6')]

## Conclusions
In this project, we have implemented a lexer using regular expressions in Python. A lexer, also known as a tokenizer or scanner, is an essential component in the compilation process of programming languages. Its primary responsibility is to break down an input string into a sequence of tokens, which are atomic units that represent meaningful language elements such as keywords, operators, literals, and identifiers. These tokens are identified based on a set of production rules that define the syntax of the language being processed.
The lexer performs the critical task of analyzing the input source code and identifying the distinct lexemes, which are the smallest units of syntax in a language. Each lexeme is then mapped to a corresponding token based on its type and semantics, as defined by the production rules. The tokens generated by the lexer form a stream of symbols that serve as input to the next stage of the compilation process, which is typically the parser.
The lexer can be viewed as a key tool in programming language processing, and it can be employed in a wide range of applications, such as syntax highlighting, code completion, and program analysis. Syntax highlighting is a feature that enhances code readability by coloring the tokens with different colors, based on their type. Code completion assists programmers by suggesting possible completions for partially typed code, based on the tokens generated by the lexer. Program analysis involves analyzing the program structure and properties to detect errors, security vulnerabilities, or optimization opportunities.
In this project, we utilized the Python programming language to develop a lexer using regular expressions. Regular expressions are a powerful tool for pattern matching and text processing, and they provide an efficient way to define the production rules for the lexer. We defined a set of regular expressions for identifying the different types of tokens, such as integers, floats, operators, parentheses, and white spaces. We also defined the corresponding token types for each regular expression, such as INT, FLOAT, OP, LPAREN, RPAREN, and SPACE.
The lexer implementation involved iterating over the input string and matching it against the regular expressions defined for each token type. If a match was found, the corresponding token was generated and added to the list of tokens generated so far. If no match was found, an error was raised indicating that the input string was invalid.
Overall, this project provides a solid foundation for understanding and implementing lexers and scanners in Python. It demonstrates the importance of the lexer in programming language processing and highlights the power and versatility of regular expressions for defining the syntax of a language. With this knowledge, one can build more sophisticated compilers, interpreters, and code analysis tools that leverage the capabilities of the lexer to facilitate language processing and improve the developer experience.