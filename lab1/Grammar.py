import random
class Grammar:
    def __init__(self, productions, start_symbol):

        self.productions = productions
        self.start_symbol = start_symbol



    def generate_string(self):
        return self._generate_string(self.start_symbol)

    def _generate_string(self, symbol):
        if symbol not in self.productions:
            return symbol
        production = random.choice(self.productions[symbol])
        return ''.join(self._generate_string(s) for s in production)

    def to_finite_automaton(self):
        # Initialize the automaton with a single start state
        start_state = 0
        automaton = {start_state: {}}
        state_count = 1

        # Add transitions for each production rule
        for symbol in self.productions:
            for production in self.productions[symbol]:
                current_state = start_state
                for s in production:
                    if s not in automaton[current_state]:
                        # Add a new state and transition
                        automaton[current_state][s] = state_count
                        automaton[state_count] = {}
                        state_count += 1
                    current_state = automaton[current_state][s]
                # Add an epsilon transition to the final state for the last symbol in the production
                if current_state not in automaton:
                    automaton[current_state] = {}
                automaton[current_state][''] = start_state

        # Return the automaton
        return automaton


# Define the grammar
productions = {
    'S': ['dS','bS','cA'],
    'A': ['aB'],
    'B': ['aB','bB','c'],

}
start_symbol = 'S'
grammar = Grammar(productions, start_symbol)

automaton = grammar.to_finite_automaton()

# Generate a string
for i in range(5):
    string = grammar.generate_string()


    print(string)
print(automaton)

