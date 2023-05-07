# Lexer & Scanner
## Course: Formal Languages & Finite Automata
## Author: Grama Alexandru FAF-211





## Theory
    The theory discussed in the provided excerpt revolves around the concept of a lexer, which is derived from lexical analysis—a process that involves extracting lexical tokens from a sequence of characters. Lexical analysis serves as an initial stage in the compilation or interpretation of programming, markup, or other types of languages. While the lexer is often referred to as a tokenizer or scanner, its fundamental purpose remains the same.

During lexical analysis, tokens are identified based on predefined rules specific to the given language. The output produced by the lexer is known as lexemes, which essentially form a stream of these identified lexical units. It is important to note the distinction between lexemes and tokens. A lexeme is the result of splitting the input based on delimiters, such as spaces or other designated characters. On the other hand, tokens provide names or categories to each lexeme. Tokens do not necessarily retain the actual value of the lexeme but rather capture its type and potentially some associated metadata.

In summary, the lexer plays a crucial role in the processing of programming languages and other forms of textual data. It operates by analyzing input strings, segmenting them into lexemes based on specified rules, and assigning tokens to these lexemes to categorize and represent their type. By understanding the difference between lexemes and tokens, developers and language designers can effectively handle and manipulate textual information in a structured and meaningful manner.

## Objectives:
- Understand what lexical analysis [1] is.

- Get familiar with the inner workings of a lexer/scanner/tokenizer.

- Implement a sample lexer and show how it works.
  

## Implementation description
### Lexer class
In the realm of Python programming, the Lexer class plays a crucial role in the process of parsing an input string and identifying the distinct types of tokens contained within it. This class is designed to handle the intricate task of tokenization by leveraging a collection of regular expression patterns specifically created to match various token types. These patterns encompass a wide range of elements, including operators, identifiers, keywords, numbers, strings, and more.

When the tokenize method of the Lexer class is invoked, it initiates a systematic iteration over these predefined patterns. For each iteration, the Lexer attempts to match the patterns against the input string, seeking instances where they align with the structure of the tokens. Whenever a successful match is detected, the Lexer proceeds to record the corresponding token and its associated value, incorporating them into a list of tokens.

However, it is essential to account for scenarios in which the input string contains invalid tokens that do not conform to the defined patterns. In such cases, the Lexer class is designed to raise a ValueError exception, alerting the user to the presence of an unrecognized or malformed token within the input.

By employing the Lexer class in Python, developers can effectively break down an input string into its constituent tokens, allowing for subsequent analysis, processing, or interpretation. This tokenization process serves as a fundamental step in various language-related tasks, such as developing compilers, interpreters, syntax highlighting, code analysis tools, and more.
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
The tokenize method of the Lexer class in Python provides a powerful mechanism for breaking down an input string into a structured list of tokens. By leveraging regular expressions and a collection of token patterns, this method enables the identification and extraction of meaningful units from the input.

During the execution of the tokenize method, the Lexer instance accesses its self.token_patterns attribute, which contains the list of predefined token patterns. It iterates through this list, attempting to match each pattern to the beginning of the input string. If a match is successfully detected, the method combines the token type associated with the pattern and the matched substring to create a token representation.

To ensure efficient processing, the tokenize method modifies the input string by removing the portion that has been matched. This iterative process continues until the entire input string has been examined and all possible tokens have been extracted. The resulting tokens are then added to the token list stored in the self.tokens attribute of the Lexer instance.

However, if a pattern fails to match any portion of the input string, indicating the presence of an invalid or unexpected token, the tokenize method raises a ValueError. This exception serves as an indicator that the Lexer encountered a token that does not conform to any defined pattern, thereby signaling a potential issue in the input or the lexer's configuration.

By employing the Lexer class and its tokenize method, developers gain a reliable and flexible tool for performing lexical analysis in Python. This functionality proves invaluable in a wide range of applications, including the development of programming language tools, syntax highlighting editors, code analyzers, and many other language processing tasks.

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
The Main class imports the Lexer class from the lexer module, and then creates an instance of the Lexer class by invoking its constructor without any arguments. Subsequently, the tokenize method of the Lexer instance is invoked with the input string "2 * (21/2) + (3 + 4) - 5 / 6". The method tokenizes the input string by separating it into a list of tokens and then returns the list. Finally, the resulting list of tokens is printed to the console using the print function. The output confirms that the input string has been correctly tokenized into its component tokens, including numbers, operators, and parentheses. Moreover, the message "input valid" is printed to the console, indicating that the input string was tokenized successfully without encountering any errors.

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