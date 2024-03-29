import matplotlib.pyplot as plt
import networkx as nx
import unittest
from Automaton.Automaton import Automaton
from Automaton.FiniteAutomaton import FiniteAutomaton
from grammar.Grammar import Grammars
from grammar.lexer import MathLexer
from Chomsky.ChomskyConverter import CNFConverter
from Parser.parser import Parser
from Parser.Interpreter import Interpreter
from Chomsky.UnitTester import UnitTester



class Main:
    print(
        '-------------------------------------------------------------------LAB1-------------------------------------------------------------------------')

    def __init__(self):
        self.productions = {
            'S': ['aS','bS','cA'],
            'A': ['aB',],
            'B': ['aB','bB','c'],
        }
        self.start_symbol = 'S'
        self.grammar = Grammars(self.productions, self.start_symbol)
        self.finite_automaton = self.grammar.to_finite_automaton()
        self.automaton = FiniteAutomaton


    def generate_strings(self, num_strings):
        for i in range(num_strings):
            string = self.grammar.generate_string()
            print(string)

if __name__ == '__main__':
    # Create a Main object
    main = Main()


    main.generate_strings(5)

    automatons = main.grammar.to_finite_automaton()

    automaton = {
        'states': {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'},
        'alphabet': {'a', 'b', 'c'},
        'transition': {
            'q0': {'a': 'q1', 'b': 'q2', 'c': 'q3'},
            'q1': {'a': 'q1', 'b': 'q2', 'c': 'q3'},
            'q2': {'a': 'q4', 'b': 'q5', 'c': 'q6'},
            'q3': {'a': 'q1', 'b': 'q2', 'c': 'q3'},
            'q4': {'a': 'q4', 'b': 'q5', 'c': 'q6'},
            'q5': {'a': 'q4', 'b': 'q5', 'c': 'q6'},
            'q6': {'a': 'q4', 'b': 'q5', 'c': 'q6'}
        },
        'start_state': 'q0',
        'final_states': {'q1', 'q2', 'q3', 'q4', 'q5', 'q6'}
    }

    checker = FiniteAutomaton(automaton)

    checker.check_strings(['aab', 'abcbb', 'bac', 'cab', 'ccaabb'])

    print(automatons)

automation = Automaton()

automation.states = ['q0', 'q1', 'q2', 'q3']
automation.alphabet = ['a', 'b', 'c']
automation.transitions = {('q0', 'a'): ['q0', 'q1'],
                        ('q1', 'b'): ['q2'],
                        ('q2', 'a'): ['q2'],
                        ('q2', 'c'): ['q0'],
                        ('q2', 'b'): ['q3']}
automation.start_state = 'q0'
automation.accept_states = ['q3']
print('')

print('-------------------------------------------------------------------LAB2-------------------------------------------------------------------------')
print('')
is_deterministic = automation.is_deterministic()
print(f"Is automaton deterministic? {is_deterministic}")

# Convert NDFA to DFA
dfa = automation.to_dfa()
print(f"DFA states: {dfa.states}")
print(f"DFA transition function: {dfa.transitions}")
print(f"DFA initial state: {dfa.start_state}")
print(f"DFA final states: {dfa.accept_states}")

grammar = automation.to_grammar()
print(f"Regular grammar productions: {grammar}")
print(main.grammar.chomsky_classification())
automation.render()
print('')
print('-------------------------------------------------------------------LAB3-------------------------------------------------------------------------')
print('')
lexer = MathLexer('2 * (21/2) + (3 + 4) - 5 / 6')
tokens = lexer.tokenize()
print(tokens)
print('')
print('-------------------------------------------------------------------LAB4-------------------------------------------------------------------------')
print('')
VN = {'S', 'A', 'B', 'C', 'D'}
VI = {'a', 'b'}
P = [
    ('S', ('A', 'C')),
    ('S', ('b', 'A')),
    ('S', ('B',)),
    ('S',('a','A')),
    ('A', ()),
    ('A', ('a', 'S')),
    ('A', ('A', 'B','a','b')),
    ('B', ('a',)),
    ('B', ('b', 'S')),
    ('C', ('a', 'b', 'C')),
    ('D', ('A', 'B'))
]
S = 'S'
grammar = (VN, VI, P, S)

# Convert the grammar to Chomsky normal form
cnf_converter = CNFConverter(grammar)
cnf_grammar = cnf_converter.convert_to_cnf()

# Print the resulting grammar
print('Original grammar:')
print(grammar)
print('Grammar in Chomsky normal form:')
print(cnf_grammar)

# print("All Tests Passed")
# unittest.main()
print('')
print('-------------------------------------------------------------------LAB5-------------------------------------------------------------------------')

lexer = MathLexer("var m = 21; var x = 3; var z = m + x;")
parser = Parser(lexer)
ast = parser.process()
print(ast)
interpreter = Interpreter()
interpreter.interpret(ast)
print(interpreter.variables)
