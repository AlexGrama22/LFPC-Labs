from FiniteAutomaton import FiniteAutomaton
from Grammar import Grammars
class Main:

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
    main = Main()
    main.generate_strings(5)
    automatons = main.grammar.to_finite_automaton()
    automaton = {
        'states': {'q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6'},
    'alphabet': {'a', 'b', 'c'},
    'transitions': {
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
