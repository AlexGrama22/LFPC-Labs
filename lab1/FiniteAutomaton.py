import random
class FiniteAutomaton:
    def __init__(self, start_state, transitions):
        self.start_state = start_state
        self.transitions = transitions

    def accepts(self, input_string):
        current_state = self.start_state

        # Iterate over each symbol in the input string
        for symbol in input_string:
            # If the symbol is not a valid transition, reject the string
            if symbol not in self.transitions[current_state]:
                return False
            # Otherwise, transition to the next state
            current_state = self.transitions[current_state][symbol]

        # If the final state has an empty string transition to the start state, accept the string
        return '' in self.transitions[current_state]

# Define the finite automaton from the grammar
start_state = 0
transitions = {
    0: {'d': 1},
    1: {'a': 2, 'd': 1},
    2: {'b': 3, 'd': 1},
    3: {'c': 4},
    4: {'a': 0, 'd': 1, '': 0},
}
automaton = FiniteAutomaton(start_state, transitions)

# Test the automaton with some example input strings
input_strings = ['dad', 'dbc', 'dabcac', 'a', 'dd']
for input_string in input_strings:
    if automaton.accepts(input_string):
        print(f"{input_string} is a valid string for the grammar")
    else:
        print(f"{input_string} is not a valid string for the grammar")